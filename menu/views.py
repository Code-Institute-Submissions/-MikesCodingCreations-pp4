from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .models import Menu
from .forms import MenuForm


def menu_list(request):
    """ Display menu list """
    menu_list = Menu.objects.all()

    context = {'menu_list': menu_list}

    return render(request, 'Menus/list.html', context)


def menu_detail(request, slug):
    """ Display menu items in detail """
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


def edit_menu(request, slug):
    """ Edit a menu item """
    menu = get_object_or_404(Menu, slug=slug)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Menu!')
            return redirect(reverse('menu:menu_list'))
        else:
            messages.error(request, 'Failed to update Menu.')
    else:
        form = MenuForm(None, instance=menu)

    template = 'Menus/edit_menu.html'
    context = {
        'form': form,
        'menu': menu,
    }

    return render(request, template, context)


def delete_menu(request, slug):
    """ Delete a menu item """
    menu = get_object_or_404(Menu, slug=slug)
    menu.delete()
    messages.success(request, f'Successfully deleted "{menu.name}".')
    return redirect(reverse('menu:menu_list'))