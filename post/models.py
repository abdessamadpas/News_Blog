from django.db import models
from django.urls import reverse

# Create your models here.

STATUS_CHOISES=(
    ('draft', 'Draft'), 
('published', 'Published')
)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug= models.SlugField(max_length=150, unique=True, verbose_name='slug')
    class Meta:
        verbose_name = 'categories'
        verbose_name_plural = 'category'

    def get_absolute_url(self):
        return reverse('category', args={self.slug})
    
    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug= models.SlugField(max_length=150, unique=True, verbose_name='slug')
    
    class Meta:
        verbose_name = 'tags'
        verbose_name_plural = 'tag'
    def get_absolute_url(self):
        return reverse('tag', args={self.slug})
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug= models.SlugField(unique=True, verbose_name='slug')
    status= models.CharField(max_length=10, choices=STATUS_CHOISES, default='draft', verbose_name='status')
    publication_date= models.DateTimeField( verbose_name='publication date')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='category')
    picture = models.ImageField(upload_to='uploads/%Y/%m/%d', verbose_name='picture')
    content = models.TextField(verbose_name='content')
    author = models.CharField( max_length=50, default = 'Anonymous', verbose_name='author')
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        verbose_name = 'posts'
        verbose_name_plural = 'post'
    def get_absolute_url(self):
        return reverse('post_detail', args={self.slug})
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    email = models.EmailField()
    message_date = models.DateTimeField()
    message = models.TextField()
    
    class Meta:
        verbose_name = 'contacts'
        verbose_name_plural = 'contact'
    def __str__(self):
        return self.name +  self.email