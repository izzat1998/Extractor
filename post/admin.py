from django.contrib import admin

# Register your models here.
from post.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    search_fields = ['title', 'content']
    filter_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
