from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse

from .models import Menu
from .forms import MenuForm


def menu_list(request):
    menu_list = Menu.objects.all()

    context = {'menu_list': menu_list}

    return render(request, 'Menus/list.html', context)


def menu_detail(request, slug):
    menu_detail = Menu.objects.get(slug=slug)

    context = {'menu_detail': menu_detail}

    return render(request, 'Menus/detail.html', context)


def add_menu(request):
    """ Add a menu item """
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a menu item!')
            return redirect('menu:menu_list')
        else:
            messages.error(request, 'Failed to add menu item.')
    else: form = MenuForm()

    template = 'Menus/add_menu.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
