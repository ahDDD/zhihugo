<template>
<div id="app">
  <MyHeader></MyHeader>
  <Container></Container>
</div>
</template>

<script>
import MyHeader from './components/common/MyHeader.vue'
import Container from './components/common/Container.vue'

export default {
  name: 'app',
  components: {
    MyHeader,
    Container
  },
  data: function() {
    return {
      active: true
    }
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
}

body {
  margin: 0;
}
</style>
