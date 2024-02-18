from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menus = Menu.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in menus]

        # self.fields['menus'].choices = friendly_names
        # for field_name, field in self.fields.items():
        #     field.widget.attr['class'] = 'border-black rounded-0'