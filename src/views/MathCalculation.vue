<template>
  <div>
    <h2>数学计算器</h2>
    <div>
      <div class="expression-container">
        <input v-model="expression" ref="expressionInput" placeholder="输入表达式" readonly @click="updateCursorPosition" />
        <span class="cursor" :style="{ left: cursorPositionPx + 'px' }"></span> <!-- 调整光标位置 -->
      </div>
      <div class="calculator">
        <button @click="appendToExpression('1')">1</button>
        <button @click="appendToExpression('2')">2</button>
        <button @click="appendToExpression('3')">3</button>
        <button @click="appendToExpression('+')">+</button>
        <button @click="appendToExpression('4')">4</button>
        <button @click="appendToExpression('5')">5</button>
        <button @click="appendToExpression('6')">6</button>
        <button @click="appendToExpression('-')">-</button>
        <button @click="appendToExpression('7')">7</button>
        <button @click="appendToExpression('8')">8</button>
        <button @click="appendToExpression('9')">9</button>
        <button @click="appendToExpression('*')">*</button>
        <button @click="appendToExpression('0')">0</button>
        <button @click="appendToExpression('/')">/</button>
        <button @click="appendToExpression(',')">,</button> <!-- 添加逗号按钮 -->
        <button @click="appendToExpression('(')">(</button>
        <button @click="appendToExpression(')')">)</button>
        <button @click="appendToExpression('sin(')">sin</button>
        <button @click="appendToExpression('cos(')">cos</button>
        <button @click="appendToExpression('tan(')">tan</button>
        <button @click="appendToExpression('log(')">log</button> <!-- 修改log按钮 -->
        <button @click="appendToExpression('ln(')">ln</button>
        <button @click="appendToExpression('e')">e</button>
        <button @click="appendToExpression('π')">π</button>
        <button @click="appendToExpression('^')">^</button>
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
      cursorPosition: 0, // 添加光标位置属性
      cursorPositionPx: 0, // 添加光标位置像素属性
      result: '',
    };
  },
methods: {
    appendToExpression(char) {
      const beforeCursor = this.expression.slice(0, this.cursorPosition);
      const afterCursor = this.expression.slice(this.cursorPosition);
      this.expression = beforeCursor + char + afterCursor;
      this.cursorPosition += char.length; // 更新光标位置
      this.updateCursorPosition(); // 更新光标位置
    },
    clearExpression() {
      this.expression = '';
      this.cursorPosition = 0; // 重置光标位置
    },
    deleteLast() {
      if (this.cursorPosition > 0) {
        const beforeCursor = this.expression.slice(0, this.cursorPosition - 1);
        const afterCursor = this.expression.slice(this.cursorPosition);
        this.expression = beforeCursor + afterCursor;
        this.cursorPosition -= 1; // 更新光标位置
        this.updateCursorPosition(); // 更新光标位置
      }
    },
    updateCursorPosition(event) {
      if (event) {
        this.cursorPosition = event.target.selectionStart; // 更新光标位置
      }
      const inputElement = this.$refs.expressionInput;
      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      context.font = window.getComputedStyle(inputElement).font;
      const text = this.expression.slice(0, this.cursorPosition);
      const width = context.measureText(text).width;
      this.cursorPositionPx = width - inputElement.scrollLeft; // 考虑滚动位置
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
.calculator {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 10px;
}
.calculator button {
  padding: 20px;
  font-size: 18px;
}
.expression-container {
  position: relative;
  display: inline-block;
  width: 100%; /* 确保容器宽度 */
  overflow: hidden; /* 隐藏溢出内容 */
}
.cursor {
  position: absolute;
  top: 0;
  width: 2px;
  height: 100%;
  background-color: black;
  animation: blink 1s step-start infinite;
}
input {
  height: 30px; /* 确保输入框高度一致 */;
  width: 99%; /* 确保输入框宽度一致 */;
  font-family: monospace; /* 使用等宽字体 */;
  overflow: auto; /* 允许滚动 */
}
@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
