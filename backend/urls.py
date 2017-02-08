from django.conf.urls import url
from views import CommentList, CommentFavePost, SubCommentPost, BigVListByAgrees, BigVListByFollowers, BigVListByThanks

urlpatterns = [
    url(r'^comment/$', CommentList.as_view()),
    url(r'^reply/$', SubCommentPost.as_view()),
    url(r'^fave/(?P<pk>\d+)/$', CommentFavePost.as_view()),
    url(r'^bigv/followers/', BigVListByFollowers.as_view()),
    url(r'^bigv/thanks/', BigVListByThanks.as_view()),
    url(r'^bigv/agrees/', BigVListByAgrees.as_view())
]