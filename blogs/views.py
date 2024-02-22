from django.shortcuts import render
from django.http import HttpRequest
from blog_app.models import *

def home(request):
    featured_post = Blog.objects.filter(is_featured=True,status='published').order_by('-update_at')
    posts = Blog.objects.filter(is_featured=False,status='published')
    print(posts)
    context = {
        "featured_post" : featured_post,
        "posts":posts
    }
    return render(request, 'index.html',context)