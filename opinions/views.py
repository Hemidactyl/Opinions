from .models import Post, Comment
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from rest_framework import permissions, status
from .serializers import (
    PostSerializer,
    CommentSerializer,
    CommentAuthorSerializer,
    DeletePostSerializer,
    AuthorCounter
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


def index(request):
    post_list = Post.objects.all().filter(is_deleted=None)
    context = {'post_list':post_list}
    return render(request, 'opinions/index.html', context)

"""
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return HttpResponse(post.author +"'s fairly pointless post")
"""

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post':post}
    return render(request, 'opinions/detail.html', context)


def reply(request, post_id):
    post = Post.objects.get(pk=post_id)
    speaker = request.POST['speaker']
    retort = request.POST['retort']
    post.comment_set.create(author=speaker, comment_text=retort)
    return HttpResponseRedirect(reverse('detail', args=[post_id]))

# view post list where is_deleted=None
class PostList(GenericAPIView, ListModelMixin):
    queryset = Post.objects.filter(is_deleted=None)
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# create new post
class CreatePost(GenericAPIView, CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# using UpdateModelMixin to 'delete' post by setting is_delete to datetime.now
# for now, have to manually change date in the API
class DeletePost(GenericAPIView, UpdateModelMixin):
    queryset = Post.objects.all()
    serializer_class = DeletePostSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# list all comments to a particular post (by post_id in the url)
class CommentList(GenericAPIView, ListModelMixin):
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id)

    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# create comment
class CreateComment(GenericAPIView, CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# delete comment
class DeleteComment(GenericAPIView, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# list of all author's with nr of posts and comments they each made
# work in progress, experimenting with serializers
'''
class AuthorList(GenericAPIView, ListModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentAuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
'''

class AuthorList(APIView):

    def get(self, request, *args, **kwargs):
        doIt = AuthorCounter(*args, **kwargs)
        result = doIt.count_authors()
        response = Response(result, status=status.HTTP_200_OK)
        return response


# Previous approaches - APIView and ModelViewSet
'''
class PostListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all posts that have not been deleted
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().filter(is_deleted=None)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create post
    def post(self, request, *args, **kwargs):
        data = {'author': request.data.get('author'),
                'post_text': request.data.get('post_text'),
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


'''
class PostDetailApiView(APIView):
    permisson_classes = [permissions.IsAuthenticated]

    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    # gets the post with given post_id
    def get(self, request, post_id, *args, **kwargs):
        post_instance = self.get_object(post_id)
        if not post_instance:
            return Response(
                {"resp": "Post with this id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostSerializer(post_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''

'''
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-pub_date').filter(is_deleted=None)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

'''
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
'''