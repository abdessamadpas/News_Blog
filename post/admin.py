from django.contrib import admin
from .models import *



# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter= ('status', 'category', 'tags')
    list_display = ('title','slug','status', 'category', 'publication_date')

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}




admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)