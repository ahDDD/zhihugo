<template lang="html">
    <data-tables :data='tableData' :has-action-col='false' :actions-def='getActionsDef()' @row-click='rowClick' :col-not-row-click='["user_token"]' action-col-width='53'>
        <el-table-column label="#" width="61px" fixed >
            <template scope="scope">
                {{ scope.$index + indexCount }}
            </template>
        </el-table-column>
        <el-table-column prop="username" label="用户名" fixed></el-table-column>
        <el-table-column prop="agrees" label="获赞同" sortable="custom"></el-table-column>
        <el-table-column prop="followers" label="被关注" sortable="custom"></el-table-column>
        <el-table-column prop="thanks" label="被感谢" sortable="custom"></el-table-column>
        <el-table-column prop="answers" label="回答数" sortable="custom"></el-table-column>
        <el-table-column prop="posts" label="分享数" sortable="custom"></el-table-column>
        <el-table-column prop="user_token" label="传送门" width="80px">
            <template scope="scope">
                <el-button type="info" size="small" @click="handleEdit(scope.$index, scope.row)">Go</el-button>
            </template>
        </el-table-column>
    </data-tables>
</template>

<script>
import DataTables from 'vue-data-tables'
import reqwest from 'reqwest'


export default {
  data() {
    return {
      tableData: [],
      dataOpt: 'followers',
      currentPage: 0
    }
  },
  created() {
    this.getBigV()
  },
  computed: {
    indexCount() {
      return (this.$children[0].currentPage - 1) * this.$children[0].internalPageSize + 1
    }
  },
  mounted() {},
  methods: {
    getBigV: function() {
      var self = this;
      reqwest({
        url: `/api/bigv/${self.dataOpt}/`,
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
        width: 19,
        def: [{
          name: '关注Top500',
          handler() {
            if (self.dataOpt == 'followers') {
              self.$message('现在已经是了')
            } else {
              self.dataOpt = 'followers'
              self.getBigV();
            }
          },
          icon: ''
        }, {
          name: '赞同Top500',
          handler() {
            if (self.dataOpt == 'agrees') {
              self.$message('现在已经是了')
            } else {
              self.dataOpt = 'agrees'
              self.getBigV();
            }
          },
          icon: ''
        }, {
          name: '感谢Top500',
          handler() {
            if (self.dataOpt == 'thanks') {
              self.$message('现在已经是了')
            } else {
              self.dataOpt = 'thanks'
              self.getBigV();
            }
          },
          icon: ''
        }]
      }
    },
    rowClick: function(row) {
        console.log(this.$children[0]);
        console.log(row);
    },
    handleEdit(index, row) {
      window.open(`https://www.zhihu.com/people/${row.user_token}`)
    }
  },
  components: {}
}
</script>

<style>
</style>
