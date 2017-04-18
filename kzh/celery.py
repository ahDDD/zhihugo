#! /usr/bin/env python
# coding: utf-8
 
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

from zhihu_oauth import ZhihuClient
# from backend.models import User
 
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kzh.settings')
app = Celery('kzh')
 
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# client = ZhihuClient()
# client.load_token('token.pkl')
#
#
# @app.task(bind=True)
# def task():
#     z = User.objects.all().order_by('-agrees')[:100]
#     for user in z:
#         p = client.people(user.user_token)
#         user.agrees = p.voteup_count
#         user.thanks = p.thanked_count
#         user.answers =  p.answer_count
#         user.followers = p.follower_count
#         user.save()