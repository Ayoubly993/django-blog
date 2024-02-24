from django.shortcuts import render

from django.http import HttpResponse

from .models import *

from django.shortcuts import get_object_or_404
from django.db.models import Q

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



def blog(request,slug):

    blog_post = get_object_or_404(Blog,slug=slug)

    context= {

        "blog": blog_post,

        }

    return render(request,"blog.html",context)

def search_engine(request):
    keyword = request.GET['keyword']
    search_post = Blog.objects.filter(Q(short_description__icontains=keyword) | Q(body_description__icontains=keyword))
    context={
        'search_post':search_post ,
        'keyword': keyword
    }
    return render(request,'search.html',context)