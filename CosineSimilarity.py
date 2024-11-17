import numpy as np
import pandas as pd
from Precision import precision

def CossineSimilarity(data, target_idx):
    # 選取前 221 個欄位
    feature_data = data.iloc[:, :221].to_numpy()
    labels = data.iloc[:, -1].to_numpy()

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

        similarity_datas.append((j, similarity, labels[j]))
    
     # 將結果轉為 DataFrame 並排序
    similarity_df = pd.DataFrame(similarity_datas, columns=['Index', 'Distance', 'Label']).sort_values(by='Distance', ascending=False)
    return similarity_df


if __name__ == '__main__':
    # data files
    unformal_file = "unformal.csv"
    fnormal_file = "fnormal.csv"

    unformal_data = pd.read_csv(unformal_file, sep=',', header=None, skiprows=1)
    fnormal_data = pd.read_csv(fnormal_file, sep=',', header=None, skiprows=1)

    precision_unf = []
    precision_fno = []
    for i in range(len(unformal_data)):
        unf_data = CossineSimilarity(unformal_data, i)
        fno_data = CossineSimilarity(fnormal_data, i)
    
        precision_unf.append(precision(unf_data, 10))
        precision_fno.append(precision(fno_data, 10))

    prec_unf_mean = np.mean(precision_unf)
    prec_fno_mean = np.mean(precision_fno)
    
    print('prec_unf: ', prec_unf_mean)
    print('prec_fno:', prec_fno_mean)
    