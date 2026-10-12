from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title',)
