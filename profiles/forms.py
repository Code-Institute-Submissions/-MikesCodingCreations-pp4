from django import forms
from .models import UserProfile
from reservation.models import Reservation

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        reservation = Reservation.objects.all()