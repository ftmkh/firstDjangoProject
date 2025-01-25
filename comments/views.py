from django.shortcuts import render, redirect, get_object_or_404
from .models import Comments
from maktab7app.models import Post


def add_comment(request , post_pid):
    if request.method =="POST":
        post = get_object_or_404(Post , id=post_pid)
        comment =Comments(post=post ,
                          name=request.POST['subject'],
                          body=request.POST['body'])
        comment.save()
        return redirect('/',pk=post.id)
