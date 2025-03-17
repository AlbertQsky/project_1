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
/* 移除样式，统一使用全局 CSS 文件 */
</style>
