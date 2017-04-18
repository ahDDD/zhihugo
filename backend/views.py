# coding=utf-8
from models import Comment, SubComment, User
from serializers import CommentSerializer, SubCommentSerializer, FaveSerializer, BigVSerializer

from rest_framework import status, generics
from utils import get_client_ip
# Create your views here.


CACHE_TTL = 60 * 15


# 查询评论
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-date')
    serializer_class = CommentSerializer


# 评论点赞
class CommentFavePost(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = FaveSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# 评论评论
class SubCommentPost(generics.CreateAPIView):
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer

    # save to comment
    def perform_create(self, serializer):
        serializer.save(reply_to=Comment.objects.get(id=self.request.data['reply_to_id']))


# 查询500关注
class BigVListByFollowers(generics.ListAPIView):
    queryset = User.objects.order_by('-followers')[0:500]
    serializer_class = BigVSerializer


# 查询500赞同
class BigVListByAgrees(generics.ListAPIView):
    queryset = User.objects.order_by('-agrees')[0:500]
    serializer_class = BigVSerializer


# 查询500感谢
class BigVListByThanks(generics.ListAPIView):
    queryset = User.objects.order_by('-thanks')[0:500]
    serializer_class = BigVSerializer

