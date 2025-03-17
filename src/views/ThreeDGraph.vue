<template>
  <div>
    <h2>三维图像</h2>
    <div id="ggb-element"></div> <!-- 样式通过全局 CSS 文件应用 -->
  </div>
</template>

<script>
export default {
  mounted() {
    this.loadGeoGebra();
  },
  methods: {
    loadGeoGebra() {
      var params = {"appName": "3D", "width": window.innerWidth, "height": 600, "showToolBar": false, "showAlgebraInput": true, "showMenuBar": false };
      var applet = new GGBApplet(params, true);
      applet.setHTML5Codebase('/GeoGebra/HTML5/5.0/web3d/');
      applet.inject('ggb-element');
    }
  },
  watch: {
    '$route' (to, from) {
      if (to.path === '/function-graph') {
        this.loadGeoGebra();
      }
    }
  }
}
</script>

<style>
/* 移除样式，统一使用全局 CSS 文件 */
</style>