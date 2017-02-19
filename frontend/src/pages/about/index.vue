<template>
<el-row :gutter="10">
  <el-col :xs="24" :sm="2" :md="2" :lg="2">
    <el-menu default-active="/about/intro" class="el-menu-vertical-demo" :router="true">
      <el-menu-item index="/about/intro">本站公告</el-menu-item>
      <el-menu-item index="/about/update">更新日志</el-menu-item>
      <el-menu-item index="/about/contact">联系我们</el-menu-item>
    </el-menu>
  </el-col>
  <el-col :xs="24" :sm="22" :md="22" :lg="20">
    <div class="markdown">
      <router-view></router-view>
    </div>
  </el-col>
</el-row>
</template>

<script>
import '../../assets/css/air.css'

export default {
  data() {
    return {}
  },
  computed: {},
  mounted() {},
  methods: {},
  components: {}
}
</script>

<style lang="css">
.about_content{
    background-color: red;
}
@media (max-width: 768px){
    .el-col-xs-24 .el-menu {
        float: left;
    }
}

</style>
