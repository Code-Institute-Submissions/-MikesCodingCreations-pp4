from django.shortcuts import render

# Create your views here.
from .models import Menu


def menu_list(request):
    menu_list = Menu.objects.all()

    context = {'menu_list': menu_list}

    return render(request, 'Menus/list.html', context)


def menu_detail(request):
    pass
