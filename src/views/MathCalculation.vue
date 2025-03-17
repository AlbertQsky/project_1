<template>
  <div>
    <h2>数学计算器</h2>
    <div>
      <div class="expression-container">
        <input v-model="expression" placeholder="输入表达式" readonly />
      </div>
      <div class="calculator">
        <!-- 数字按钮 -->
        <button @click="appendToExpression('1')">1</button>
        <button @click="appendToExpression('2')">2</button>
        <button @click="appendToExpression('3')">3</button>
        <button @click="appendToExpression('4')">4</button>
        <button @click="appendToExpression('5')">5</button>
        <button @click="appendToExpression('6')">6</button>
        <button @click="appendToExpression('7')">7</button>
        <button @click="appendToExpression('8')">8</button>
        <button @click="appendToExpression('9')">9</button>
        <button @click="appendToExpression('0')">0</button>

        <!-- 运算符按钮 -->
        <button @click="appendToExpression('+')">+</button>
        <button @click="appendToExpression('-')">-</button>
        <button @click="appendToExpression('*')">*</button>
        <button @click="appendToExpression('/')">/</button>
        <button @click="appendToExpression('^')">^</button>

        <!-- 特殊符号按钮 -->
        <button @click="appendToExpression('(')">(</button>
        <button @click="appendToExpression(')')">)</button>
        <button @click="appendToExpression(',')">,</button>

        <!-- 函数按钮 -->
        <button @click="appendToExpression('sin(')">sin</button>
        <button @click="appendToExpression('cos(')">cos</button>
        <button @click="appendToExpression('tan(')">tan</button>
        <button @click="appendToExpression('log(')">log</button>
        <button @click="appendToExpression('ln(')">ln</button>

        <!-- 常量按钮 -->
        <button @click="appendToExpression('e')">e</button>
        <button @click="appendToExpression('π')">π</button>

        <!-- 操作按钮 -->
        <button @click="clearExpression">C</button>
        <button @click="deleteLast">删除</button>
        <button @click="calculate">计算</button>
      </div>
      <p>结果: {{ result }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      expression: '',
      result: '',
    };
  },
  methods: {
    appendToExpression(char) {
      const beforeCursor = this.expression;
      this.expression = beforeCursor + char;
    },
    clearExpression() {
      this.expression = '';
    },
    deleteLast() {
      this.expression = this.expression.slice(0, -1);
    },
    async calculate() {
      try {
        console.log('Sending request to calculate:', this.expression);
        const expression = this.expression.replace(/\^/g, '**');
        const response = await axios.post('http://localhost:5000/api/calculate', { expression });
        console.log('Response received:', response.data);
        this.result = response.data.result;
      } catch (error) {
        console.error('Error during calculation:', error);
        this.result = error.response?.data?.error || '计算错误';
      }
    }
  }
}
</script>

<style>
/* 移除光标相关样式 */
.expression-container {
  display: inline-block;
  width: 100%;
  overflow: hidden;
}
</style>
