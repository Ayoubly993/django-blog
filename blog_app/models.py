from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    ("draft",'Draft'),
    ("published",'Published')
)
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural= 'categories'
    def __str__(self):
        return self.category_name
    
class Blog(models.Model):
    title = models.CharField( max_length=150)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='upload/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    body_description = models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    