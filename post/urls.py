from django.contrib import admin
from django.urls import path, include

from . import views
from django.views.generic import TemplateView

urlpatterns = [
  #  path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('tags/<str:tag_slug>/', views.tags, name='tag'),
    path('post/<str:slug>/', views.PostDetail, name='post_detail'),

]
