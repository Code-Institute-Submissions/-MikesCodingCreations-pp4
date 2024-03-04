from django.shortcuts import render
from .models import AboutUs, History, Why_Choose_Us, Chef

# Create your views here.
def aboutus_list(request):
    about = AboutUs.objects.first()
    history = History.objects.first()
    why_choose_us = Why_Choose_Us.objects.all()
    chef = Chef.objects.all()

    context = {
        'about' : about,
        'history' : history,
        'why_choose_us' : why_choose_us,
        'chef' : chef
    }

    return render(request, 'aboutus/about.html', context)