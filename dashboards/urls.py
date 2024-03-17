from django.urls import path
from . import views
print('yes')
urlpatterns = [
    path('',views.bashboard,name="dashboard"),
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_category,name='add_category'),
    path('categories/edit/<int:pk>',views.edit_category,name='edit_category'),
    path('categories/delete/<int:pk>',views.delete_category,name='delete'),
    path('posts/',views.posts,name="posts"),
    path('logout',views.logout),
]
