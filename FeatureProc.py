import os
import pandas as pd
import numpy as np

# input ouput file setting
input_dir = "raw_features"
unformal_file = "unformal.csv"
fnormal_file = "fnormal.csv"
fnormal_zScore_file = "fnormal_zScore_file.csv"

# 讀檔
data = pd.DataFrame()
for file_name in os.listdir(input_dir):
    if file_name.endswith(".txt"):  
        file_path = os.path.join(input_dir, file_name)
        current_data = pd.read_csv(file_path, sep=' ', header=None, skiprows=1)
        
        # 合併數據到 data 中
        data = pd.concat([data, current_data], ignore_index=True)


# remove columns
columns_to_remove = list(range(80, 336)) + [len(data.columns) - 4]
print(columns_to_remove)
data = data.drop(columns=columns_to_remove)

# save file
data.to_csv(unformal_file, index=False)
print(f"\nsave to: {unformal_file}")

data_min_max = data
data_z_score = data

### 正歸化 Min-Max
numerical_columns = data_min_max.select_dtypes(include=np.number).columns
for col in numerical_columns:
    col_min = data_min_max[col].min()
    col_max = data_min_max[col].max()
    
    # col_max - col_min != 0
    if col_max != col_min:
        data_min_max[col] = (data_min_max[col] - col_min) / (col_max - col_min)
    else:
        data_min_max[col] = 0.0

# save file
data_min_max.to_csv(fnormal_file, index=False)
print(f"\nsave to: {fnormal_file}")


#### Z-score
numerical_columns = data_z_score.select_dtypes(include=np.number).columns
for col in numerical_columns:
    col_mean = data_z_score[col].mean()
    col_std = data_z_score[col].std()
    if col_std != 0: 
        data_z_score[col] = (data_z_score[col] - col_mean) / col_std
    else:
        data_z_score[col] = 0.0
        
# save file
data_z_score.to_csv(fnormal_zScore_file, index=False)
print(f"\nsave to: {fnormal_zScore_file}")

