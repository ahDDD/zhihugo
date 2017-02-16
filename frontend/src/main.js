// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import routeConfig from './router-config'
import Element from 'element-ui'
import DataTables from 'vue-data-tables'
// import 'element-ui/lib/theme-default/index.css'


//加载中间件
Vue.use(VueRouter)
Vue.use(Element)
Vue.use(DataTables)

//定义路由
const router = new VueRouter({
  routes: routeConfig
})

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: {
    App
  }
})
