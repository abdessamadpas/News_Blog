from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from post.forms import ContactForm
from .models import *
from django.utils import timezone
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
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        category_name = category.title
        articles = articles.filter(category=category)

    template = loader.get_template('category.html')
    
    context = {
        'articles': articles,
        'categories': categories,
        'category_name': category_name,
    }
    return HttpResponse(template.render(context, request))

def tags(request, tag_slug):
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags=tag)
        tag_name = tag.title

    template = loader.get_template('tags.html')
    
    context = {
        'articles': articles,
        'categories': categories,
        'tag_name': tag_name,
    }
    return HttpResponse(template.render(context, request))

def PostDetail(request, detail_post_slug):
    article = get_object_or_404(Post, slug=detail_post_slug)
    post_categoy = article.category
    template = loader.get_template('post_details.html')
    
    context = {
        'article': article,
        'post_categoy': post_categoy,
    }
    return HttpResponse(template.render(context, request))

def Contact(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
            msg =form.save(commit=False)
            msg.contact_date = timezone.now()
            msg.save()
            return HttpResponseRedirect('contactsuccess')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
