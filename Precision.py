import numpy as np
import pandas as pd

def precision(data: pd.DataFrame, num: int=10) -> float:
    '''
    data: pd.DataFrame(), 已排序後的距離資料, 第一筆是target
    num: The number of data items calculated
    
    return: (float)precision
    ''' 
    print('rec:', data)
    target_label = data.iloc[0, -1]
    print(f"Target label: {target_label}")
    
    count = 0
    for i in range(1, num+1):
        if data.iloc[i, -1] == target_label:
            count += 1
    
    return float(count)/float(num)
        
    
    
    