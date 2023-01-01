from django.contrib import admin
from django.urls import path, include

from . import views
#from django.views.generic import TemplateView

urlpatterns = [
  #  path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('tags/<slug:tag_slug>/', views.tags, name='tag'),
    path('post/<slug:post_slug>/', views.PostDetail, name='post_detail'),

]
