from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('reservation-management/', views.reservation_management, name='reservation_management'),
]
