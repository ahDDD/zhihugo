from models import Comment, SubComment, User
from serializers import CommentSerializer, SubCommentSerializer, FaveSerializer, BigVSerializer
from django.views.decorators.cache import cache_page

from rest_framework import status, generics
from utils import get_client_ip
# Create your views here.


CACHE_TTL = 60 * 15


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-date')
    serializer_class = CommentSerializer


class CommentFavePost(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = FaveSerializer

    def put(self, request, *args, **kwargs):
        ip = get_client_ip(request)
        print ip
        return self.update(request, *args, **kwargs)


class SubCommentPost(generics.CreateAPIView):
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer

    # save to comment
    def perform_create(self, serializer):
        serializer.save(reply_to=Comment.objects.get(id=self.request.data['reply_to_id']))


class BigVListByFollowers(generics.ListAPIView):
    queryset = User.objects.order_by('-followers')[0:500]
    serializer_class = BigVSerializer


class BigVListByAgrees(generics.ListAPIView):
    queryset = User.objects.order_by('-agrees')[0:500]
    serializer_class = BigVSerializer


class BigVListByThanks(generics.ListAPIView):
    queryset = User.objects.order_by('-thanks')[0:500]
    serializer_class = BigVSerializer

