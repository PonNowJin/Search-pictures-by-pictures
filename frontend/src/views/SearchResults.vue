<template>
  <div>
    <h1>搜尋結果</h1>
    <h2>Precision: {{ precision }}</h2>
    <div class="container">
      <div v-for="result in results" :key="result.imgPath" class="image-wrapper">
        <img :src="result.imgPath" />
        <p>距離: {{ result.score }}</p>
        <div class="category-name">{{ result.label }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
data() {
  return {
    results: [],
    precision: 0,
  };
},
computed: {
},
mounted() {
    const encodedResults = this.$route.query.results;
    this.precision = this.$route.query.precision;

    if (encodedResults) {
        // 解碼並解析 JSON 字串
        const decodedResults = JSON.parse(decodeURIComponent(encodedResults));
        console.log("Decoded Results:", decodedResults);
        this.results = decodedResults;
        console.log(this.results);

        // 使用 decodedResults 進行渲染或其他操作
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
  height: 320px;  /* 設定圖片區域的高度，保證有足夠的空間顯示文字 */
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
</style>