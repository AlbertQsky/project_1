<template>
  <div>
    <h2>三维图像</h2>
    <div id="ggb-element" style="width: 100%; height: 600px;"></div>
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