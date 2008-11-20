from django.contrib import admin

from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'pub_date',)
    search_fields = ('title', 'body')
    date_hierarchy = 'pub_date'

admin.site.register(BlogPost, BlogPostAdmin)
