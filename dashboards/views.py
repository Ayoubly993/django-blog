from django.shortcuts import render,redirect,get_object_or_404
from blog_app.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import *

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

def posts(request):
    return render(request,"dashboard/posts.html")

def logout(request):
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
    print(category)
    return render(request,'dashboard/edit_categories.html',context)