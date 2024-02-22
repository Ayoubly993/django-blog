from .models import *

def get_context(request):
    category = Category.objects.all()
    return dict(categories=category)