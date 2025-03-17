<template>
  <div>
    <nav>
      <router-link to="/function-graph/2d">二维图像</router-link>
      <router-link to="/function-graph/3d">三维图像</router-link>
    </nav>
    <h1>函数图像</h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'FunctionGraph'
}
</script>
