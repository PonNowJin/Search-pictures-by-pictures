import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    initialize_features()  # 初始化特徵資料
    app.run(host='0.0.0.0', port=8066, debug=True)
