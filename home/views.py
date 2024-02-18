from django.shortcuts import render
from menu.models import Menu
from aboutus.models import AboutUs, History, Why_Choose_Us, Chef
# Create your views here.


def home(request):
    about = AboutUs.objects.last()
    history = History.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    menu = Menu.objects.all()
    menu_list = Menu.objects.all()

    context = {
        'about' : about,
        'history' : history,
        'menu' : menu,
        'menu_list' : menu_list,
        'why_choose_us' : why_choose_us,
    }

    return render(request, 'home/index.html', context)



