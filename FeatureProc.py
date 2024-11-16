import os
import pandas as pd
import numpy as np

# input ouput file setting
input_dir = "raw_features"
unformal_file = "unformal.csv"
fnormal_file = "fnormal.csv"

# 讀檔
data = pd.DataFrame()
for file_name in os.listdir(input_dir):
    if file_name.endswith(".txt"):  
        file_path = os.path.join(input_dir, file_name)
        current_data = pd.read_csv(file_path, sep=' ', header=None, skiprows=1)
        
        # 合併數據到 data 中
        data = pd.concat([data, current_data], ignore_index=True)


# remove columns
columns_to_remove = list(range(80, 336)) + [len(data.columns) - 3]
data = data.drop(columns=columns_to_remove)


# save file
data.to_csv(unformal_file, index=False)
print(f"\nsave to: {unformal_file}")

# 正歸化
numerical_columns = data.select_dtypes(include=np.number).columns
for col in numerical_columns:
    col_min = data[col].min()
    col_max = data[col].max()
    
    # col_max - col_min != 0
    if col_max != col_min:
        data[col] = (data[col] - col_min) / (col_max - col_min)
    else:
        data[col] = 0.0


# save file
data.to_csv(fnormal_file, index=False)
print(f"\nsave to: {fnormal_file}")
