import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sys
from EuclideanDistance import EuclideanDistance
from CosineSimilarity import CosineSimilarity
from Pcc import pcc
from Precision import precision
import random
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

IMG_FOLDER = "images/"  # 圖片資料夾
feature_data = {}
features_dict = {}

# 初始化時計算每個類別資料夾中的圖片
def initialize_features():
    global features_dict
    allowed_extensions = {'jpg', 'jpeg', 'png'}  # 允許的圖片格式
    for category in os.listdir(IMG_FOLDER):
        cat_path = os.path.join(IMG_FOLDER, category)
        if os.path.isdir(cat_path):
            features_dict[category] = []
            for img_file in os.listdir(cat_path):
                # 確保是有效的圖片文件
                if img_file.split('.')[-1].lower() in allowed_extensions:
                    img_path = os.path.join(cat_path, img_file)
                    features_dict[category].append(img_path)
                    
                    
def search_images(img_path, method, normalized, num=11):
    '''
    img_path: 完整路徑
    method: 'ED', 'CS', 'PCC'
    normalized: 0 (無正規化), 1(min-max), 2(zScore)
    '''
    file_name = os.path.basename(img_path)
    distance_df = pd.DataFrame()
    
    if method == 'ED':
        distance_df = EuclideanDistance(file_name=file_name, normalized=normalized)
    elif  method == 'CS':
        distance_df = CosineSimilarity(file_name=file_name, normalized=normalized)
    else:
        distance_df = pcc(file_name=file_name, normalized=normalized)
    
    p = precision(distance_df, num-1)
    
    result_file = distance_df.iloc[:num,:]   # 前11列
    results = []
    
    for index, result in result_file.iterrows():
        imgPath = os.path.join(IMG_FOLDER, result['Label'], result['FileName'])
        score = result[1]
        results.append({"imgPath": imgPath, "score": score, "label": result['Label'], "precision": p})
        
    print('results:', results)    
    return results, p


# 使用 send_file 返回圖片
@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = list(features_dict.keys())
    random_images = {cat: random.choice(features_dict[cat]) for cat in categories}  # 隨機選擇每類別中的一張圖片
    
    # 返回圖片的路徑給前端，前端可以向這些路徑發送請求
    return jsonify({"categories": random_images})

# 提供圖片的靜態文件
@app.route('/images/<path:filename>')
def get_image(filename):
    image_path = os.path.join(IMG_FOLDER, filename)
    if os.path.exists(image_path):
        return send_file(image_path)  # 使用 send_file 返回圖片
    else:
        return jsonify({"error": "File not found"}), 404
    
# 搜尋相似圖片
@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    img_path = data.get('imgPath')
    method = data.get('method')
    normalized = data.get('normalized')

    # 搜尋相似圖片
    results, p = search_images(img_path, method, normalized)

    # 返回搜尋結果，圖片路徑和相似度
    for result in results:
        result['imgPath'] = f"http://localhost:8066/{result['imgPath']}"

    return jsonify({'results': results, 'precision': p})

if __name__ == '__main__':
    initialize_features()  # 初始化特徵資料
    app.run(host='0.0.0.0', port=8066, debug=True)
