from django.shortcuts import render
from .models import AboutUs, History, Why_Choose_Us, Chef

# Create your views here.
def aboutus_list(request):
    about = AboutUs.objects.last()
    history = History.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    chef = Chef.objects.last()

    context = {
        'about' : about,
        'history' : history,
        'why_choose_us' : why_choose_us,
        'chef' : chef
    }

    # if why_choose_us:
    #     context['why_choose_us'] = why_choose_us
    # else:
    #     context['why_choose_us'] = None

    return render(request, 'aboutus/about.html', context)
