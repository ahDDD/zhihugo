// 引入组件
import bigV from './pages/bigv/index.vue'
import comment from './pages/comment/index.vue'
import about from './pages/about/index.vue'

import intro from './docs/intro.md'
import update from './docs/update.md'
import contact from './docs/contact.md'

export default [{
  // 配置路由，当路径为'/bigv',使用组件bigV
  path: '/bigv',
  component: bigV,
}, {
  path: '/comment',
  component: comment
}, {
  path: '/about',
  component: about,
  children: [{
    path: '',
    component: intro
  }, {
    path: 'intro',
    component: intro
  }, {
    path: 'update',
    component: update
  }, {
    path: 'contact',
    component: contact
  }]
}]
