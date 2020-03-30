from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    search_fields = ['name', 'description', 'url']
    list_filter = ['createdOn']
    list_display = ['name', 'description', 'url']


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("headline",)}
    search_fields = ['headline', 'description', 'tags']
    list_filter = ['createdOn']
    list_display = ['headline', 'tags', 'createdBy']


admin.site.register(Post, PostAdmin)
