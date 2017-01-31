<template>
<div id="app">
  <header>
    <el-row type="flex" justify="space-between" class="ui container">
      <el-col :span="6">
        <div>
          <a href="#">
            <h1>看知乎</h1>
          </a>
        </div>
      </el-col>
      <el-col :span="18" class="nav">
        <el-menu theme="dark" default-active="/bigv" mode="horizontal" :router="true" class="high">
          <el-menu-item index="/bigv" :class="{'isActive': active}">大v排行</el-menu-item>
          <el-menu-item index="/comment" :class="{'isActive': !active}">留言板</el-menu-item>
          <el-menu-item index="/tougao" :class="{'isActive': !active}">投稿</el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </header>
  <main>
      <div class="ui container">
          <router-view class="view"></router-view>
      </div>
  </main>
</div>
</template>

<script>
export default {
  name: 'app',
  components: {
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

h1 {
  margin: 0;
  line-height: 80px;
}

header {
  height: 80px;
  background-color: #324057;
}

header h1 a {
  display: block;
}

.el-menu {
  background-color: transparent;
  float: right;
}

.high.el-menu--horizontal .el-menu-item {
  font-weight: 700;
  line-height: 75px;
  height: 100%;
}

.menu {
  background-color: #F9FAFC;
}

main {
    padding-top: 35px;
    padding-bottom: 35px;
}
</style>
