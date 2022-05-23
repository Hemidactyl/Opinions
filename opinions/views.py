from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post#, Comment

def index(request):
    post_list = Post.objects.all()
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