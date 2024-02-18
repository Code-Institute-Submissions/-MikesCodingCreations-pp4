

from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<slug:slug>', views.menu_detail, name='menu_detail'),
    # path('<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path('add/', views.add_menu, name='add_menu'),
]
