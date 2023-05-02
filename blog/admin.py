from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status','created_date', 'published_date', 'updated_date')
    list_filter=('status','author','created_date','published_date')
    search_fields=('title','text')
    prepopulated_fields={'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy= 'published_date'
    ordering = ('status', 'published_date')