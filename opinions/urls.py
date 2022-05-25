from django.urls import path, include
from .views import (
    PostList,
    CreatePost,
    DeletePost,
    CreateComment,
    CommentList,
    DeleteComment,
    AuthorList
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/reply/', views.reply, name='reply'),
    path('postlist', PostList.as_view(), name='postlist'),
    path('createpost', CreatePost.as_view(), name='createpost'),
    path('deletepost/<int:pk>', DeletePost.as_view(), name='deletepost'),
    path('createcomment', CreateComment.as_view(), name='createcomment'),
    path('commentlist/<int:post_id>', CommentList.as_view(), name='commentlist'),
    path('deletecomment/<int:pk>', DeleteComment.as_view(), name='deletecomment'),
    path('authorlist', AuthorList.as_view(), name='authorlist')
]