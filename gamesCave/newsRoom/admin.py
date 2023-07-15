from django.contrib import admin
from . models import News

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'short_body', 'publish', 'created', 'updated', 'status']
    list_filter = ['title', 'author', 'publish']
    search_fields = ['title', 'author', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    def short_body(self, obj):
        short_body = obj.body.split()[:10]
        return ' '.join(short_body)
    