<template>
    <div>
      <h1>搜尋結果</h1>
      <div v-for="result in results" :key="result.imgPath">
        <img :src="result.imgPath" style="width:100px;" />
        <p>相似度: {{ result.score }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        results: []
      };
    },
    created() {
      this.results = JSON.parse(this.$route.query.results);
    }
  };
  </script>
  