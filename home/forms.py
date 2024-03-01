from django import forms
from .models import Order
  
class InputForm(forms.Form):

    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())