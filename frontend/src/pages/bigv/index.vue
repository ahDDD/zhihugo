<template lang="html">
    <div class="ui container">
        <el-table :data="tableData" border style="width: 100%" :default-sort="{prop: 'date', order: 'descending'}">
            <el-table-column prop="date" label="ID" sortable width="180">
            </el-table-column>
            <el-table-column prop="name" label="赞数" sortable width="180">
            </el-table-column>
            <el-table-column prop="address" label="个人主页" :formatter="formatter">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
  data () {
    return {}
  },
  computed: {},
  mounted () {},
  methods: {},
  components: {}
}
</script>

<style lang="css">
</style>
