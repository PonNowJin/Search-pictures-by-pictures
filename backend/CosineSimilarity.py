import numpy as np
import pandas as pd
from Precision import precision

def CosineSimilarity(data:pd.DataFrame=None, target_idx:int=None, file_name='', normalized:int=None):
    '''
    data: pd.DataFrame()
    target_idx: int
    file_name: str
    normalized: 0 (無正規化), 1(min-max), 2(zScore)
    '''
    unformal_file = "unformal.csv"
    minMax_file = "fnormal.csv"
    zScore_file = "fnormal_zScore_file.csv"
    
    if not data:
        if normalized==0:
            data = pd.read_csv(unformal_file, sep=',', header=None, skiprows=1)
        elif normalized==1:
            data = pd.read_csv(minMax_file, sep=',', header=None, skiprows=1)
        else:
            data = pd.read_csv(zScore_file, sep=',', header=None, skiprows=1)
    
    # 選取前 221 個欄位
    feature_data = data.iloc[:, :221].to_numpy()
    labels = data.iloc[:, -1].to_numpy()
    file_names = data.iloc[:, -3].to_numpy()
    
    # 獲取 target_row
    if file_name:
        try:
            target_idx = np.where(file_names == file_name)[0][0]
            target_row = feature_data[target_idx]
        except IndexError:
            raise ValueError(f"File name '{file_name}' not found in the data.")
    else:
        target_row = feature_data[target_idx]

    similarity_datas = []
    
    norm_A = np.sqrt(np.sum(target_row**2))
    for j in range(len(feature_data)):
        # 計算cos similarity
        norm_B = np.sqrt(np.sum(feature_data[j]**2))
        
        if norm_A==0 or norm_B==0:
            similarity = 0
        else:
            dot_product = np.sum(target_row * feature_data[j])
            similarity = dot_product/(norm_A * norm_B)

        similarity_datas.append((j, similarity, file_names[j], labels[j]))
    
     # 將結果轉為 DataFrame 並排序
    similarity_df = pd.DataFrame(similarity_datas, columns=['Index', 'Distance', 'FileName', 'Label']).sort_values(by='Distance', ascending=False)
    return similarity_df


if __name__ == '__main__':
    '''
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
    
    for i in range(len(unformal_data)):
        unf_data = CosineSimilarity(unformal_data, i)
        minMax_data_temp = CosineSimilarity(minMax_data, i)
        zScore_data_temp = CosineSimilarity(zScore_data, i)
    
        precision_unf.append(precision(unf_data, 10))
        precision_minMax.append(precision(minMax_data_temp, 10))
        precision_zScore.append(precision(zScore_data_temp, 10))
        

    prec_unf_mean = np.mean(precision_unf)
    prec_minMax_mean = np.mean(precision_minMax)
    prec_zScore_mean = np.mean(precision_zScore)
    
    print('prec_unf: ', prec_unf_mean)
    print('prec_minMax:', prec_minMax_mean)
    print('prec_zScore:', prec_zScore_mean)
    '''
    print(CosineSimilarity(file_name='BWimage_047.jpg', normalized=1))
    