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


# this is just here to test some basic principles
class CommentAuthorSerializer(serializers.ModelSerializer):
    a_number = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['pk', 'author', 'a_number']

    def get_a_number(self, obj):
        return 666


# should strictly be in a different file, but should work for now
# custom class to create a dictionary of all authors + the number of posts
# and comments they made and return a list of strings for output.
class AuthorCounter(object):

    def __init__(self, *args, **kwargs):
        pass

    def count_authors(self):
        all_posts = Post.objects.filter(is_deleted=None)
        all_comments = Comment.objects.all()

        author_dict = {}

        for post in all_posts:
            if post.author not in author_dict:
                author_dict[post.author] = [1,0]
            else:
                author_dict[post.author][0] += 1

        for comment in all_comments:
            if comment.author not in author_dict:
                author_dict[comment.author] = [0,1]
            else:
                author_dict[comment.author][1] += 1

        result = []
        for author in author_dict:
            result.append(f"{author}: {author_dict[author][0]} post(s) and {author_dict[author][1]} comment(s).")


        return result
        




'''
class PostAuthorSerializer(serializers.ModelSerializer):
    comment_author = CommentAuthorSerializer(many=True, read_only=True)
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['pk', 'author', 'comment_author']

    def get_post_count(self, obj):
        author_dict = {}
        
        return author_dict
'''

