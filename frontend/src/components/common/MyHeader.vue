<template>
    <header>
      <el-row type="flex" justify="space-between" class="ui container">
        <el-col :span="8">
            <router-link to="/bigv">
              <!--<img src="../../assets/images/vector_space_illust.svg" />-->
              <h1>知乎Go</h1>
            </router-link>
        </el-col>
        <el-col :span="16" class="nav">
          <el-menu theme="dark" default-active="bigv" mode="horizontal" :router="true" class="high">
            <el-menu-item index="bigv" :class="{'isActive': active}">
                大v排行
            </el-menu-item>
            <el-menu-item index="comment" :class="{'isActive': !active}">
                留言板
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-row>
    </header>
</template>

<script>
export default {
  data () {
    return {
        active: true
    }
  },
  computed: {},
  mounted () {},
  methods: {},
  components: {}
}
</script>

<style lang="css">
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
</style>
