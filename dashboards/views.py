from django.shortcuts import render,redirect,get_object_or_404
from blog_app.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import *
from django.utils.text import slugify

# Create your views here.

@login_required(login_url="login")
def bashboard(request):
    category_count= Category.objects.all().count()
    blogs_count= Blog.objects.all().count()
    context={
        'categorys_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request,"dashboard/dashboard.html",context)

def categories(request):
    return render(request,"dashboard/categories.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request,'dashboard/add_category.html',context)

def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context ={
        'form':form,
        'category':category,
        }
    return render(request,'dashboard/edit_categories.html',context)

# posts crud
def posts(request):
    posts = Blog.objects.all()
    context={
        'posts' : posts
    }
    return render(request,"dashboard/posts.html",context)
def edit_posts(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = BlogForm(instance=post)
    context={
        'form':form,
        'post':post
    }
    return render(request,'dashboard/edit_post.html',context)

def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.author = request.user
            post.save()
            post.slug = slugify(post.title)+"-"+str(post.id)
            form.save() 
            return redirect('posts')
        else:
            print(form.errors)
    form = BlogForm()
    context={
        'form':form
    }

    return render(request,'dashboard/add_new_post.html',context)

def delete_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')
def logout(request):
    return render(request,"dashboard/categories.html")
