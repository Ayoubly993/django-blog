from django.shortcuts import render,redirect
from django.http import HttpRequest
from blog_app.models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 
def home(request):
    featured_post = Blog.objects.filter(is_featured=True,status='published').order_by('-update_at')
    posts = Blog.objects.filter(is_featured=False,status='published')
    context = {
        "featured_post" : featured_post,
        "posts":posts
    }
    return render(request, 'index.html',context)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = RegistrationForm()
    context={
        "form":form
    }
    return render(request,"register.html",context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)
def logout(request):
    auth.logout(request)
    return redirect("home")