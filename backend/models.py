from __future__ import unicode_literals

from django.db import models

# Create your models here.
from six import python_2_unicode_compatible

@python_2_unicode_compatible
class Comment(models.Model):
    author = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    faves = models.IntegerField(default=0)
    email = models.EmailField()
    url = models.CharField(max_length=100, null=True, blank=True)
    reply = models.BooleanField(default=False)

    def __str__(self):
        return self.text


@python_2_unicode_compatible
class SubComment(models.Model):
    author = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    faves = models.IntegerField(default=0)
    email = models.EmailField()
    url = models.CharField(max_length=100, null=True, blank=True)
    reply_to = models.ForeignKey(Comment, related_name='subcomments', null=True, blank=True)

    def __str__(self):
        return self.text


class Url(models.Model):
    md5_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url'

@python_2_unicode_compatible
class User(models.Model):
    user_token = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    business = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    employment = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    agrees = models.IntegerField(blank=True, null=True)
    thanks = models.IntegerField(blank=True, null=True)
    asks = models.IntegerField(blank=True, null=True)
    answers = models.IntegerField(blank=True, null=True)
    posts = models.IntegerField(blank=True, null=True)
    followees = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    hashid = models.CharField(db_column='hashId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.username