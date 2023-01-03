from django.urls import path

from post.views import index, category, tags, PostDetail, ContactSuccess, Contact_page
#from django.views.generic import TemplateView

urlpatterns = [
  #  path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', index, name='index'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('tags/<slug:tag_slug>/', tags, name='tag'),
    path('contact/', Contact_page, name='contact'),
    path('contact/success/', ContactSuccess, name='contact_success'),
    path('<slug:detail_post_slug>/', PostDetail, name='post_detail'),


]
