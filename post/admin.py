from django.contrib import admin
from .models import *



# Register your models here.
class CategoryArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
class PostArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
class TagArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}




admin.site.register(Category, CategoryArticleAdmin)
admin.site.register(Tag, TagArticleAdmin)
admin.site.register(Post, TagArticleAdmin)
