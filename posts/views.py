from django.shortcuts import render
from .models import Post

def post_home(request):
    # retrive all posts from the Post model
    posts=Post.objects.all().order_by("date")
    return render(request, "posts/post_home.html",{'posts':posts})
