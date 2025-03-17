import { createRouter, createWebHistory } from 'vue-router'
import MathCalculation from '../views/MathCalculation.vue'
import FunctionGraph from '../views/FunctionGraph.vue'
import IntegralCalculation from '../views/IntegralCalculation.vue'
import TwoDGraph from '../views/TwoDGraph.vue' // 导入二维图像组件
import ThreeDGraph from '../views/ThreeDGraph.vue' // 导入三维图像组件
import Math from '../views/Math.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/math',
      name: 'Math',
      component: Math,
      children: [
        {
          path: 'calculation',
          name: 'MathCalculation',
          component: MathCalculation
        },
        {
          path: 'integral',
          name: 'IntegralCalculation',
          component: IntegralCalculation
        }
      ]
    },
    {
      path: '/function-graph',
      name: 'FunctionGraph',
      component: FunctionGraph,
      children: [
        {
          path: '2d',
          name: 'TwoDGraph',
          component: TwoDGraph
        },
        {
          path: '3d',
          name: 'ThreeDGraph',
          component: ThreeDGraph
        }
      ]
    }
  ],
})

export default router
