from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('category=<slug:category>', views.post_by_category, name='post_by_category'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]
