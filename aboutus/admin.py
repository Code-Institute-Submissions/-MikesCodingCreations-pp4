from django.contrib import admin

# Register your models here.
from .models import AboutUs, History, Why_Choose_Us, Chef




admin.site.register(AboutUs)
admin.site.register(History)
admin.site.register(Why_Choose_Us)
admin.site.register(Chef)