from .models import Category, Post, Comment
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class PostModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ['title', 'content']
#     list_filter = ('status', 'created_on',)
#     prepopulated_fields = {'slug': ('title',)}
#     summernote_fields = ('content',)

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)