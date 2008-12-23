from django.contrib import admin

from attachments.admin import AttachmentInline
from blog.models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'pub_date',)
    search_fields = ('title', 'body')
    date_hierarchy = 'pub_date'
    inlines = (AttachmentInline,)


admin.site.register(BlogPost, BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)