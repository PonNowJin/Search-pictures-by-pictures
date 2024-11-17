<template>
  <div id="app">
    <!-- 頂部導航欄 -->
    <header>
      <nav class="navbar">
        <h1>圖片搜尋系統</h1>
        <ul>
          <li><router-link to="/">首頁</router-link></li>
        </ul>
      </nav>
    </header>

    <!-- 主要內容區域 -->
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #42b983;
  padding: 10px 20px;
}

.navbar h1 {
  color: white;
  margin: 0;
}

.navbar ul {
  list-style: none;
  display: flex;
  padding: 0;
}

.navbar li {
  margin: 0 10px;
}

.navbar a {
  color: white;
  text-decoration: none;
}

main {
  padding: 20px;
}
</style>
