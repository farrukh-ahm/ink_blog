from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('author', 'title'),}
    list_display = ['title', 'slug', 'author',
                    'excerpt', 'content', 'created_on',
                    'edited_on', 'featured_image',
                    'status'
    ]
    list_filter = ['author', 'status']
    search_fields = ['author', 'title']
    actions = ['status']
    summernote_fields = ['content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['commented_by', 'commented_post', 'commented_text',
                    'created_on', 'approved'
    ]
    list_filter = ['approved']
    actions = ['approved']


# @admin.register(Subscribe)
# class SubscribeAdmin(admin.ModelAdmin):
#     list_display = ['subscriber', 'sub_to']
