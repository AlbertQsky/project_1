<template>
  <div>
    <h2>定积分计算（上下限仅支持输入浮点数）</h2>
    <input v-model="func" placeholder="输入函数" />
    <select v-model="numVariables">
      <option value="1">一元</option>
      <option value="2">二元</option>
      <option value="3">三元</option>
    </select>
    <div v-if="numVariables >= 1">
      <input v-model="variables.x.lower" placeholder="x下限" />
      <input v-model="variables.x.upper" placeholder="x上限" />
    </div>
    <div v-if="numVariables >= 2">
      <input v-model="variables.y.lower" placeholder="y下限" />
      <input v-model="variables.y.upper" placeholder="y上限" />
    </div>
    <div v-if="numVariables >= 3">
      <input v-model="variables.z.lower" placeholder="z下限" />
      <input v-model="variables.z.upper" placeholder="z上限" />
    </div>
    <button @click="integrate">计算定积分</button>
    <p>结果: {{ integralResult }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      func: 'sin(x)',
      numVariables: 1, // 添加变量元数
      variables: {
        x: { lower: '0', upper: '3.141592653' },
        y: { lower: '', upper: '' },
        z: { lower: '', upper: '' }
      },
      integralResult: ''
    };
  },
  methods: {
    async integrate() {
      try {
        const limits = [];
        if (this.numVariables >= 1) {
          limits.push({ variable: 'x', lower: parseFloat(this.variables.x.lower), upper: parseFloat(this.variables.x.upper) });
        }
        if (this.numVariables >= 2) {
          limits.push({ variable: 'y', lower: parseFloat(this.variables.y.lower), upper: parseFloat(this.variables.y.upper) });
        }
        if (this.numVariables >= 3) {
          limits.push({ variable: 'z', lower: parseFloat(this.variables.z.lower), upper: parseFloat(this.variables.z.upper) });
        }
        const response = await axios.post('http://localhost:5000/api/integrate', {
          function: this.func,
          limits: limits
        });
        this.integralResult = response.data.result;
      } catch (error) {
        this.integralResult = error.response?.data?.error || '计算错误';
      }
    }
  }
}
</script>

<style>
/* 移除样式，统一使用全局 CSS 文件 */
</style>
