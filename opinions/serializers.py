from .models import Post, Comment
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['pk','author', 'post_text']

class DeletePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['is_deleted']



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['post', 'author', 'comment_text']


class CommentAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['pk', 'author']


class PostAuthorSerializer(serializers.ModelSerializer):
    comment_author_set = CommentAuthorSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = ['pk', 'author', 'comment_author_set']


