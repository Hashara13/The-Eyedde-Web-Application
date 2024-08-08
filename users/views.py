from django.shortcuts import render,redirect
#from .models import Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_page(request):
    
    if request.method =="POST": # if method was post and user is validated redirect user to home page
        form=UserCreationForm(request.POST) # this instance is for validate the user
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('post_home')
    else:
        form=UserCreationForm()
    return render(request, "users/signup.html",{'form':form})

def login_page(request):
    
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST) 
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('post_home')
    else:
        form=AuthenticationForm()
    return render(request, "users/login.html",{'form':form})

def logout_page(request): 
    if request.method =="POST":
        logout(request)
        return redirect('post_home')
