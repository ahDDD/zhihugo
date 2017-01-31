from django.conf.urls import url
from views import CommentList, CommentFavePost, SubCommentPost

urlpatterns = [
    url(r'^comment/$', CommentList.as_view()),
    url(r'^reply/$', SubCommentPost.as_view()),
    url(r'^fave/(?P<pk>\d+)/$', CommentFavePost.as_view())
]