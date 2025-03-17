<template>
  <div id="app">
    <nav>
      <router-link to="/math">数学计算</router-link>
      <router-link to="/function-graph">函数图像</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* 添加一些基本样式 */
nav {
  display: flex;
  gap: 10px;
}
</style>
