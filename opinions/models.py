from django.utils import timezone

from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50)
    post_text = models.TextField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author + "'s post"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    comment_text = models.TextField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author + "'s comment"