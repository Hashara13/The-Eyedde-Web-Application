from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

def post_home(request):
    # retrive all posts from the Post model
    posts=Post.objects.all().order_by("date")
    return render(request, "posts/post_home.html",{'posts':posts})

def post_content(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request, "posts/post_content.html",{'post':post})
@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method=='POST':
        form=forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('post_home')
        
    else:
        form=forms.CreatePost()
    return render(request, "posts/post_create.html",{'form':form})
