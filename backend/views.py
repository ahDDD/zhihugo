from models import Comment, SubComment
from serializers import CommentSerializer, SubCommentSerializer, FaveSerializer

from rest_framework import status, generics
from rest_framework.response import Response
# Create your views here.


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-date')
    serializer_class = CommentSerializer


class CommentFavePost(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = FaveSerializer


class SubCommentPost(generics.CreateAPIView):
    queryset = SubComment.objects.all()
    serializer_class = SubCommentSerializer

    # save to comment
    def perform_create(self, serializer):
        serializer.save(reply_to=Comment.objects.get(id=self.request.data['reply_to_id']))