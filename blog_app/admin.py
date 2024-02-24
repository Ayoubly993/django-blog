from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title',)}
    list_display = ('title','author','category','is_featured','status')
    search_fields = ('title','id','category__category_name')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(SocialMediaLinks) 