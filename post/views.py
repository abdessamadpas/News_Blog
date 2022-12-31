from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import *
# Create your views here.
def index(request):
    #articles = Post.objects.filter(status='published').order_by('-publication_date')
    articles = Post.objects.order_by('-publication_date')
    categories = Category.objects.all()
    template = loader.get_template('index.html')
    
    context = {
        'articles': articles,
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def category(request, category_slug):
    articles = Post.objects.filter(slug=category_slug).order_by('-publication_date')
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)

    template = loader.get_template('category.html')
    
    context = {
        'articles': articles,
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def tags(request, tag_slug):
    articles = Post.objects.filter(slug=tag_slug).order_by('-publication_date')
    categories = Category.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags=tag)

    template = loader.get_template('tags.html')
    
    context = {
        'articles': articles,
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))