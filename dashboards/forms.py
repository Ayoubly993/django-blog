from django import forms
from blog_app.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_description','body_description','status','is_featured')