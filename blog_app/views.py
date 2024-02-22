from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def post_by_category(request,category_id):
    posts = Blog.objects.filter(status='published',category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return render(request,'eror.html')
    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)