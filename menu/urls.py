

from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<slug:slug>', views.menu_detail, name='menu_detail'),
    path('add/', views.add_menu, name='add_menu'),
    # path('edit/', views.edit_menu, name='edit_menu'),
    path('edit/<slug:slug>/', views.edit_menu, name='edit_menu'),
]
