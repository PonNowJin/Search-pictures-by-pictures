similarity_datas.append((j, similarity, file_name[j], labels[j]))
    
     # 將結果轉為 DataFrame 並排序
    similarity_df = pd.DataFrame(similarity_datas, columns=['Index', 'Distance', 'FileName', 'Label']).sort_values(by='Distance')