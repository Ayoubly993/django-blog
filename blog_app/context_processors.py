from .models import *

def get_context(request):
    category = Category.objects.all()
    return dict(categories=category)

def get_SocialMediaLinks(request):
    links = SocialMediaLinks.objects.all()
    return dict(links=links)