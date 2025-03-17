<template>
  <div>
    <nav>
      <router-link to="/math/calculation">数学计算</router-link>
      <router-link to="/math/integral">积分计算</router-link>
    </nav>
    <h1>数学计算</h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Math'
}
</script>
