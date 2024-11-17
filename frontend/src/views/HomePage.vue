<template>
  <div>
    <h1>圖片搜尋</h1>
    <div>
      <label>相似度計算方式：</label>
      <select v-model="method">
        <option value="ED">歐幾里德距離</option>
        <option value="CS">Cosine Similarity</option>
        <option value="PCC">PCC</option>
      </select>
      <label>   是否正規化：</label>
      <select v-model="normalized">
        <option value="0">無正規化</option>
        <option value="1">min-max</option>
        <option value="2">zScore</option>
      </select>
    </div>
    
    <div>
      <h1>類別選擇</h1>
      <div class="container">
        <div v-for="(imgPath, category) in categories" :key="category" class="image-wrapper" @click="searchCategory(category)">
          <img :src="'http://localhost:8066/' + imgPath" :alt="category" />
          <div class="category-name">{{ category }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        method: 'ED',
        normalized: 0,
        categories: {}
      };
    },
    async created() {
      const response = await axios.get('http://127.0.0.1:8066/api/categories');
      this.categories = response.data.categories;
      console.log(this.categories)
    },
    methods: {
      async searchCategory(category) {
        const imgPath = this.categories[category];
        console.log(imgPath)
        const data = {
          imgPath,
          method: this.method,
          normalized: this.normalized
        };
        const response = await axios.post('http://127.0.0.1:8066/api/search', data);
        console.log(response);
        // 將結果轉換為 JSON 字串
        const resultsString = JSON.stringify(response.data.results);

        // 使用 encodeURIComponent 編碼以防止特殊字符影響 URL
        const encodedResults = encodeURIComponent(resultsString);

        // 將編碼後的結果作為查詢參數傳遞
        this.$router.push({
            name: 'Results',
            query: { results: encodedResults, precision: response.data.precision }
        });
      }
    }
  };
  </script>
  
  <style scoped>
/* 容器 */
.container {
  display: flex;
  flex-wrap: wrap;  /* 允許換行 */
  justify-content: space-evenly;  /* 使圖片均勻分布 */
  gap: 20px;  /* 圖片之間的間隙 */
}

/* 每張圖片 */
.image-wrapper {
  width: 250px;  /* 設定圖片區域的寬度 */
  height: 250px;  /* 設定圖片區域的高度，保證有足夠的空間顯示文字 */
  display: flex;
  flex-direction: column;  /* 使圖片和文字垂直排列 */
  justify-content: space-between;  /* 保證圖片和文字之間有間隙 */
  align-items: center;
  text-align: center;  /* 讓文字居中顯示 */
  padding: 10px;  /* 增加內邊距，避免文字貼近邊緣 */
  box-sizing: border-box;  /* 包括內邊距在內計算寬度和高度 */
  background-color: #f4f4f4;  /* 可以增加背景顏色，讓圖片和文字更明顯 */
  border-radius: 8px;  /* 可選：圓角 */
  overflow: hidden;  /* 防止圖片超出邊界 */
  cursor: pointer;
}

/* 圖片 */
.image-wrapper img {
  width: 100%;  /* 使圖片寬度自適應容器 */
  max-height: 200px;  /* 設定圖片最大高度 */
  object-fit: contain;  /* 保證圖片保持原始比例且不變形 */
  margin-bottom: 10px;  /* 讓圖片和文字之間有些間隔 */
}

/* 類別名稱 */
.category-name {
  margin-top: 8px;  /* 讓類別名稱與圖片間有點距離 */
  font-size: 14px;  /* 設定字型大小 */
  color: #333;  /* 設定字體顏色 */
  font-weight: bold;  /* 可以加粗字體 */
}

label {
  font-size: 20px;  /* 設定 label 的字體大小 */
  color: #555;  /* 設置顏色 */
  margin-right: 0px;  /* 設定 label 與後續元素之間的間距 */
  margin-left: 10px;
}

select {
  font-size: 18px;
}
</style>
