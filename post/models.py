from django.db import models

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
    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug= models.SlugField(max_length=150, unique=True, verbose_name='slug')
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug= models.SlugField(unique=True, verbose_name='slug')
    status= models.CharField(max_length=10, choices=STATUS_CHOISES, default='draft', verbose_name='status')
    publication_date= models.DateTimeField(auto_now_add=True, verbose_name='publication date')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='category')
    picture = models.ImageField(upload_to='uploads/%Y/%m/%d', verbose_name='picture')
    content = models.TextField(verbose_name='content')
    author = models.CharField( max_length=50, default = 'Anonymous', verbose_name='author')
    tags = models.ManyToManyField('Tag', blank=True)
       
    
    def __str__(self):
        return self.title