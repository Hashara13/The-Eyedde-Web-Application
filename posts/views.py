from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def post_home(request):
    # retrive all posts from the Post model
    posts=Post.objects.all().order_by("date")
    return render(request, "posts/post_home.html",{'posts':posts})

def post_content(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request, "posts/post_content.html",{'post':post})
