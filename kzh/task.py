# coding=utf-8
from __future__ import absolute_import, unicode_literals
import datetime, json
from djcelery import models as celery_models
from django.utils import timezone
from celery import shared_task
from zhihu_oauth import ZhihuClient
from backend.models import User
from zhihu_oauth.exception import NeedCaptchaException



# try:
#     client.login('ddsweet520@live.com', '123321')
#     client.save_token('token.pkl')
# except NeedCaptchaException:
#     with open('a.gif', 'wb') as f:
#         f.write(client.get_captcha())
#     captcha = input('please input captcha:')
#     client.login('email_or_phone', 'password', captcha)
#
# p = client.people('hideinthewoods')
# print p.favorite_count # 收藏
# print p.thanked_count # 获得感谢
# print p.voteup_count # 获得赞同
# print p.follower_count # 被关注
# print p.answer_count # 回答数
# print p.collected_count # 被收藏数

@shared_task()
def task():
    client = ZhihuClient()
    client.load_token('token.pkl')
    z = User.objects.all().order_by('-agrees')[:100]
    for user in z:
        p = client.people(user.user_token)
        user.agrees = p.voteup_count
        user.thanks = p.thanked_count
        user.answers =  p.answer_count
        user.followers = p.follower_count
        user.save()


def create_task(name, task, task_args, crontab_time):
    '''
    创建任务
    name       # 任务名字
    task       # 执行的任务 "myapp.tasks.add"
    task_args  # 任务参数  {"x":1, "Y":1}
    crontab_time # 定时任务时间 格式：
	    {
	      'month_of_year': 9  # 月份
	      'day_of_month': 5   # 日期
	      'hour': 01         # 小时
	      'minute':05  # 分钟
	    }

    '''
    # task任务， created是否定时创建
    task, created = celery_models.PeriodicTask.objects.get_or_create(
        name=name,
        task=task)
    # 获取 crontab
    crontab = celery_models.CrontabSchedule.objects.filter(
        **crontab_time).first()
    if crontab is None:
        # 如果没有就创建，有的话就继续复用之前的crontab
        crontab = celery_models.CrontabSchedule.objects.create(
            **crontab_time)
    task.crontab = crontab # 设置crontab
    task.enabled = True # 开启task
    task.kwargs = json.dumps(task_args) # 传入task参数
    expiration = timezone.now()
    task.expires = expiration # 设置任务过期时间为现在时间的一天以后
    task.save()
    return True


def disable_task(name):
    '''
    关闭任务
    '''
    try:
        task = celery_models.PeriodicTask.objects.get(name=name)
        task.enabled = False # 设置关闭
        task.save()
        return True
    except celery_models.PeriodicTask.DoesNotExist:
        return True