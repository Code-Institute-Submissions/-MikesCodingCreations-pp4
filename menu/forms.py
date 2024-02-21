from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = "__all__"
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menus = Menu.objects.all()
