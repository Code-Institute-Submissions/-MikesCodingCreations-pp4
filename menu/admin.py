from django.contrib import admin

# Register your models here.

from django_summernote.admin import SummernoteModelAdmin
from .models import Menu


class MenuModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'


admin.site.register(Menu, MenuModelAdmin)