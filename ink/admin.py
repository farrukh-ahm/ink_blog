from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.unregister(SocialAccounts)

# admin.site.unregister(User)
# admin.site.register(User)


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


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