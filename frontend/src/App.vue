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
  @import url(http://fonts.googleapis.com/css?family=Open+Sans:300italic,300);
  font-family: "Open Sans", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  font-weight: 300;
}

body {
  margin: 0;
  color: #444;
  line-height: 1.85;
}
</style>
