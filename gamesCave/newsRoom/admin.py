from django.contrib import admin
from . models import News

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status']
    list_filter = ['title', 'author', 'body', 'publish']
    search_fields = ['title', 'author', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']