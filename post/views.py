from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from post.forms import ContactForm
from post.models import Post, Category, Tag, Contact
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #articles = Post.objects.filter(status='published').order_by('-publication_date')
    articles = Post.objects.order_by('-publication_date')
    categories = Category.objects.all()
    #TODO: pagination
    pagination = Paginator(articles, 2)
    page_number = request.GET.get('page')
    articles_paginated = pagination.get_page(page_number)

    template = loader.get_template('index.html')
    
    context = {
        'articles': articles_paginated,
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

def Contact_page(request):

    contact = Contact.objects.all()
    print(contact)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save(commit=False)
            contact_form.message_date = timezone.now()
            contact_form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    
    return render(request, 'contact.html', context)

#static website for the form contact

def ContactSuccess(request):
	return render(request, 'contactSuccess.html',)
