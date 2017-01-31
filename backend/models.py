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