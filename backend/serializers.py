from rest_framework import serializers
from models import Comment, SubComment

class SubCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubComment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    subcomments = SubCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'date', 'text', 'faves', 'email', 'url', 'reply', 'subcomments')


class FaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('faves',)