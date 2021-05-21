
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index , name = 'index'),
    path('about/', views.about , name = 'about'),
    path('contact/', views.contact , name = 'contact'),
    path('blog/', views.blog , name = 'blog'),
    path('blog_single/<int:id>', views.blog_single , name = 'blog_single'),
    path('gallery/', views.gallery , name = 'gallery'),
    path('service/', views.service , name = 'service'),
    path('newsletter_post/', views.newletter , name = 'newsletterpost'),
    # path('post-newletters/', views.newletter , name = 'newletterspost'),
]