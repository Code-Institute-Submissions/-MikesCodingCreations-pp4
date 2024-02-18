from .models import Category, Post, Comment
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class PostModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)