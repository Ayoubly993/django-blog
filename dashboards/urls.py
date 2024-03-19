from django.urls import path
from . import views
print('yes')
urlpatterns = [
    path('',views.bashboard,name="dashboard"),
    # categories crud
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_category,name='add_category'),
    path('categories/edit/<int:pk>',views.edit_category,name='edit_category'),
    path('categories/delete/<int:pk>',views.delete_category,name='delete'),
    # posts crud
    path('posts/',views.posts,name="posts"),
    path('posts/edit/<int:pk>',views.edit_posts,name='edit_post'),
    path('posts/add',views.add_post,name='add_new_post'),
    path('posts/delete/<int:pk>',views.delete_post,name='delete_post'),
    path('logout',views.logout),
]
