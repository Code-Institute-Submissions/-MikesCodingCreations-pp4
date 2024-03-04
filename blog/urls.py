from django.urls import path, include
from . import views
from .views import post_list, post_detail, post_by_category


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('category/<str:category>/', post_by_category, name='post_by_category'),
    path('add/', views.add_post, name='add_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]
