<template>
<div class="ui comments">
  <h2 class="ui dividing header">留言板</h2>
  <div class="comment" v-for="comment in comments">
    <a class="avatar">
      <img :src="avatarImg">
    </a>
    <div class="content">
      <a class="author" v-if="comment.url" :href="comment.url">{{comment.author}}</a>
      <a class="author" v-else>{{comment.author}}</a>
      <div class="metadata">
        <span class="date">{{dateFormat(comment.date)}}</span>
      </div>
      <div class="text">
        {{comment.text}}
      </div>
      <div class="actions">
        <a class="reply" @click="comment.reply = !comment.reply">Reply</a>
        <a class="rating" @click="postFave(comment)">
          <i class="star icon"></i> {{comment.faves}} Faves
        </a>
      </div>
      <el-form label-position="top" :model="replyForm" :rules="rules" ref="ruleForm" class="sub" v-if="comment.reply">
        <el-form-item label="评论" prop="text">
          <el-input type="textarea" v-model="replyForm.text"></el-input>
        </el-form-item>
        <el-form-item>
          <el-col :span="11">
            <el-form-item label="你的大名" prop="author">
              <el-input v-model="replyForm.author"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="11">
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="replyForm.email"></el-input>
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="域名" prop="url">
          <el-input v-model="replyForm.url"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitReplyForm(replyForm, comment)">回复</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="comments" v-if="comment.subcomments != '[]'">
      <div class="comment" v-for="subcomments in comment.subcomments">
        <a class="avatar">
          <img :src="avatarImg">
        </a>
        <div class="content">
          <a class="author" v-if="subcomments.url" :href="subcomments.url">{{subcomments.author}}</a>
          <a class="author" v-else>{{subcomments.author}}</a>
          <div class="metadata">
            <span class="date">{{dateFormat(subcomments.date)}}</span>
          </div>
          <div class="text">
            {{subcomments.text}}
          </div>
          <div class="actions">
            <!-- <a class="reply" @click="subcomment.reply = !subcomment.reply">Reply</a> -->
            <a class="rating" @click="postFave(comment.faves)">
              <i class="star icon"></i> {{subcomments.faves}} Faves
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <h2 class="ui dividing header">发表评论</h2>
  <el-form label-position="top" :model="ruleForm" :rules="rules" ref="ruleForm">
    <el-form-item label="评论" prop="text">
      <el-input type="textarea" v-model="ruleForm.text"></el-input>
    </el-form-item>
    <el-form-item>
      <el-col :span="11">
        <el-form-item label="你的大名" prop="author">
          <el-input v-model="ruleForm.author"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="11">
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="ruleForm.email"></el-input>
        </el-form-item>
      </el-col>
    </el-form-item>
    <el-form-item label="域名" prop="url">
      <el-input v-model="ruleForm.url"></el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleForm)">评论</el-button>
    </el-form-item>
  </el-form>
</div>
</template>

<script>
import avatarImg from 'assets/steve.jpg'
import reqwest from 'reqwest'
import moment from 'moment'

import {
  Message
} from 'element-ui';

export default {
  data() {
    return {
      avatarImg: avatarImg,
      comments: [{
        reply: false,
        author: 'Matt',
        date: 'Today at 5:42PM',
        text: 'How artistic!',
        faves: '5',
        subcomments: [{
          reply: false,
          author: 'D',
          date: 'Justnow',
          text: 'Matt How artistic!',
          faves: '1'
        }, {
          reply: false,
          author: 'Gigi',
          date: 'Justnow',
          text: 'D How artistic!',
          faves: '2'
        }, ]
      }],
      ruleForm: {
        author: '',
        email: '',
        text: '',
        url: ''
      },
      replyForm: {
        author: '',
        email: '',
        text: '',
        url: ''
      },
      rules: {
        text: [{
          required: true,
          message: '评论不能为空',
          trigger: 'blur'
        }, {
          max: 140,
          message: '长度在 140 个字符以内',
          trigger: 'blur'
        }],
        author: [{
          required: true,
          message: '大名不能为空',
          trigger: 'blur'
        }, {
          max: 100,
          message: '长度在 10 个字符以内',
          trigger: 'blur'
        }],
        email: [{
          required: true,
          message: '请输入邮箱地址',
          trigger: 'blur'
        }, {
          type: 'email',
          message: '请输入正确的邮箱地址',
          trigger: 'blur,change'
        }],
        url: [{
          type: 'url',
          message: '请输入正确的域名',
          trigger: 'blur,change'
        }]
      }
    }
  },
  computed: {},
  created() {
    this.getComment();
  },
  mounted() {},
  methods: {
    getComment: function() {
      var self = this;
      reqwest({
        url: 'http://127.0.0.1:8000/api/comment/',
        type: 'json',
        method: 'get',
        error: function(err) {},
        success: function(resp) {
          self.comments = resp;
        }

      })
    },
    submitForm: function(data) {
      var self = this;
      reqwest({
        url: 'http://127.0.0.1:8000/api/comment/',
        type: 'json',
        method: 'post',
        data: {
          author: data.author,
          email: data.email,
          text: data.text,
          url: data.url
        },
        error: function(err) {
          Message({
            message: err,
            type: 'error'
          })
        },
        success: function(resp) {
          Message.success({
            message: '评论成功',
            type: 'success'
          })
          self.comments.unshift(resp);
          self.ruleForm.author = '',
            self.ruleForm.email = '',
            self.ruleForm.text = '',
            self.ruleForm.url = ''
        }
      })
    },
    submitReplyForm: function(data, comment) {
      var self = this;
      reqwest({
        url: 'http://127.0.0.1:8000/api/reply/',
        type: 'json',
        method: 'post',
        data: {
          author: data.author,
          email: data.email,
          text: data.text,
          url: data.url,
          reply_to_id: comment.id
        },
        error: function(err) {
          Message({
            message: err,
            type: 'error'
          })
        },
        success: function(resp) {
          Message.success({
            message: '回复成功',
            type: 'success'
          })
          comment.reply = false;
          comment.subcomments.unshift(resp)
        }
      })
    },
    postFave: function(comment) {
      reqwest({
        url: `http://127.0.0.1:8000/api/fave/${comment.id}/`,
        type: 'json',
        method: 'put',
        data: {
          faves: comment.faves + 1
        },
        error: function(err) {
          Message({
            message: err.responseText,
            type: 'error'
          })
          console.log(err);
        },
        success: function(resp) {
          comment.faves = resp.faves
        }
      })
    },
    dateFormat: function(date) {
        moment.locale('zh-cn');
      return moment(date, moment.ISO_8601).fromNow()
    }
  },
  components: {}
}
</script>

<style>
.el-col.el-col-11:last-child {
  float: right;
}

.sub {
  background-color: #E5E9F2;
  padding: 20px 10px 10px;
  margin-top: 10px;
}
</style>
