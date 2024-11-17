import numpy as np
import pandas as pd
from Precision import precision
import os

def EuclideanDistance(data, target_idx):
    # 選取前 221 個欄位
    feature_data = data.iloc[:, :221].to_numpy()
    labels = data.iloc[:, -1].to_numpy()
    file_name = data.iloc[:, -3].to_numpy()

    target_row = feature_data[target_idx]
    # print('target_row:', target_row)

    distances = []

    for j in range(len(feature_data)):
        # 計算歐幾里得距離
        distance = np.sqrt(np.sum((target_row - feature_data[j]) ** 2))
        distances.append((j, distance, file_name[j], labels[j]))

    # 將結果轉為 DataFrame 並排序
    distance_df = pd.DataFrame(distances, columns=['Index', 'Distance', 'FileName', 'Label']).sort_values(by='Distance')

    # print("與其他行的歐幾里得距離:")
    # print(distance_df)
    return distance_df
    
if __name__ == '__main__':
    # data files
    unformal_file = "unformal.csv"
    minMax_file = "fnormal.csv"
    zScore_file = "fnormal_zScore_file.csv"
    

    unformal_data = pd.read_csv(unformal_file, sep=',', header=None, skiprows=1)
    minMax_data = pd.read_csv(minMax_file, sep=',', header=None, skiprows=1)
    zScore_data = pd.read_csv(zScore_file, sep=',', header=None, skiprows=1)

    precision_unf = []
    precision_minMax = []
    precision_zScore = []
    
    
    # 創建資料夾結構
    output_dir = "Outputs/ED"  # 主資料夾
    subfolders = ['unf', 'min-max', 'z-score']  # 子資料夾
    
    # 確保主資料夾和子資料夾存在
    os.makedirs(output_dir, exist_ok=True)
    for subfolder in subfolders:
        os.makedirs(os.path.join(output_dir, subfolder), exist_ok=True)
    
    for i in range(len(unformal_data)):
        unf_data = EuclideanDistance(unformal_data, i)
        minMax_data_temp = EuclideanDistance(minMax_data, i)
        zScore_data_temp = EuclideanDistance(zScore_data, i)
    
        precision_unf.append(precision(unf_data, 10))
        precision_minMax.append(precision(minMax_data_temp, 10))
        precision_zScore.append(precision(zScore_data_temp, 10))
        
        # 儲存為 CSV
        fileName = unf_data['FileName'][i]
        unf_data.to_csv(os.path.join(output_dir, 'unf', f'{fileName}.csv'), index=False)
        minMax_data_temp.to_csv(os.path.join(output_dir, 'min-max', f'{fileName}.csv'), index=False)
        zScore_data_temp.to_csv(os.path.join(output_dir, 'z-score', f'{fileName}.csv'), index=False)


    prec_unf_mean = np.mean(precision_unf)
    prec_minMax_mean = np.mean(precision_minMax)
    prec_zScore_mean = np.mean(precision_zScore)
    
    print('prec_unf: ', prec_unf_mean)
    print('prec_minMax:', prec_minMax_mean)
    print('prec_zScore:', prec_zScore_mean)


