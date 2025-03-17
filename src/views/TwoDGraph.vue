<template>
  <div>
    <h2>二维图像</h2>
    <input v-model="function2D" placeholder="输入二维函数" />
    <button @click="plot2D">绘制二维图像</button>
    <button @click="toggleHelp">显示函数说明</button>
    <div v-if="showHelp">
      <h3>函数示例</h3>
      <ul>
        <li>二次函数: x**2</li>
        <li>正弦函数: Math.sin(x)</li>
        <li>余弦函数: Math.cos(x)</li>
        <li>正切函数: Math.tan(x)</li>
        <li>对数函数: Math.log(x)</li>
        <li>自然对数: Math.log(x)</li>
        <li>常数 e: Math.e</li>
        <li>常数 π: Math.PI</li>
      </ul>
    </div>
    <div id="plot2D"></div>
  </div>
</template>

<script>
import * as plotly from 'plotly.js-dist';

export default {
  data() {
    return {
      function2D: 'Math.sin(x)',
      showHelp: false
    };
  },
  methods: {
    toggleHelp() {
      this.showHelp = !this.showHelp;
    },
    plot2D() {
      const trace = {
        x: [...Array(100).keys()].map(x => x / 10),
        y: [...Array(100).keys()].map(x => eval(this.function2D.replace(/x/g, x / 10))),
        type: 'scatter'
      };
      const data = [trace];
      plotly.newPlot('plot2D', data);
    }
  }
}
</script>

<style>
/* 移除样式，统一使用全局 CSS 文件 */
</style>
