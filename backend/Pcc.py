import numpy as np
import pandas as pd
from Precision import precision

def pcc(data:pd.DataFrame=None, target_idx:int=None, file_name='', normalized:int=None):
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
    
    target_mean = np.mean(target_row)
    norm_x = np.sqrt(np.sum((target_row - target_mean)**2))
    for j in range(len(feature_data)):
        y_mean = np.mean(feature_data[j])
        norm_y = np.sqrt(np.sum((feature_data[j] - y_mean)**2))
        
        if norm_x==0 or norm_y==0:
            pcc_val = 0
        else:
            xy = np.sum((target_row - target_mean) * (feature_data[j] - y_mean))
            pcc_val = xy/(norm_x * norm_y)
    
        similarity_datas.append((j, pcc_val, file_names[j], labels[j]))
    
     # 將結果轉為 DataFrame 並排序
    similarity_df = pd.DataFrame(similarity_datas, columns=['Index', 'Distance', 'FileName', 'Label']).sort_values(by='Distance', ascending=False)
    return similarity_df


if __name__ == '__main__':
    """
    # data files
    unformal_file = "unformal.csv"
    fnormal_file = "fnormal.csv"

    unformal_data = pd.read_csv(unformal_file, sep=',', header=None, skiprows=1)
    fnormal_data = pd.read_csv(fnormal_file, sep=',', header=None, skiprows=1)

    precision_unf = []
    precision_fno = []
    for i in range(len(fnormal_data)):
        unf_data = pcc(unformal_data, i)
        fno_data = pcc(fnormal_data, i)
    
        precision_unf.append(precision(unf_data, 10))
        precision_fno.append(precision(fno_data, 10))

    prec_unf_mean = np.mean(precision_unf)
    prec_fno_mean = np.mean(precision_fno)
    
    print('prec_unf: ', prec_unf_mean)
    print('prec_fno:', prec_fno_mean)
    """
    
    print(pcc(file_name='BWimage_047.jpg', normalized=1))