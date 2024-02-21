from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from reservation.models import Reservation

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
        else:
            messages.error(request, "Update failed.")
    else:
        form = UserProfileForm(instance=profile)        
    reservation = profile.Reservation.all()

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)