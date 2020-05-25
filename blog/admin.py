from django.contrib import admin
from .models import Post

# Register your models here.
# Change admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','data']
    list_filter = ['data']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)