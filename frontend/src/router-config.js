// 引入组件
import bigV from './pages/bigv/index.vue'
import comment from './pages/comment/index.vue'
import about from './pages/about/index.vue'

export default [{
  // 配置路由，当路径为'/bigv',使用组件bigV
  path: '/bigv',
  component: bigV,
}, {
  path: '/comment',
  component: comment
}, {
  path: '/about',
  component: about
}]
