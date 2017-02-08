<template lang="html">
    <div class="ui container">
        <data-tables :data='tableData' :has-action-col='false' :actions-def='getActionsDef()' @row-click='rowClick' :col-not-row-click='["user_token"]'>
        <el-table-column prop="username" label="用户名"></el-table-column>
        <el-table-column prop="agrees" label="获赞同" sortable="custom"></el-table-column>
        <el-table-column prop="followers" label="被关注" sortable="custom"></el-table-column>
        <el-table-column prop="thanks" label="被感谢" sortable="custom"></el-table-column>
        <el-table-column prop="answers" label="回答数" sortable="custom"></el-table-column>
        <el-table-column prop="posts" label="分享数" sortable="custom"></el-table-column>
        <el-table-column prop="user_token" label="传送门">
            <template scope="scope">
              <el-button type="info" size="small" @click="handleEdit(scope.$index, scope.row)">走起</el-button>
            </template>
        </el-table-column>
      </data-tables>
    </div>
</template>

<script>
import DataTables from '../../components/common/DataTable.vue'
import reqwest from 'reqwest'


export default {
  data() {
    return {
      tableData: [],
      dataOpt: 'followers'
    }
  },
  created() {
    this.getBigV()
  },
  computed: {},
  mounted() {},
  methods: {
    getBigV: function() {
      var self = this;
      reqwest({
        url: `http://127.0.0.1:8000/api/bigv/${self.dataOpt}/`,
        type: 'json',
        methods: 'get',
        error: function(err) {
          Message({
            message: '获取数据失败',
            type: 'error'
          })
        },
        success: function(resp) {
          self.tableData = resp;
        }
      })
    },
    urlformatter: function(row, column) {
      return `https://www.zhihu.com/people/${row.user_token}`
    },
    getCheckFilterDef: function() {
      return {

      }
    },
    getActionsDef: function() {
      let self = this
      return {
        width: 10,
        def: [{
          name: '关注Top100',
          handler() {
            if(self.dataOpt=='followers'){
                self.$message('现在已经是了')
            }else{
                self.dataOpt='followers'
                self.getBigV();
            }
          },
          icon: ''
      },{
        name: '赞同Top100',
        handler() {
          if(self.dataOpt=='agrees'){
              self.$message('现在已经是了')
          }else{
              self.dataOpt='agrees'
              self.getBigV();
          }
        },
        icon: ''
    },{
      name: '感谢Top100',
      handler() {
        if(self.dataOpt=='thanks'){
            self.$message('现在已经是了')
        }else{
            self.dataOpt='thanks'
            self.getBigV();
        }
      },
      icon: ''
    }]
      }
    },
    rowClick: function(row) {

    },
    handleEdit(index, row) {
      window.open(`https://www.zhihu.com/people/${row.user_token}`)
    },
  },
  components: {}
}
</script>

<style lang="css">
</style>
