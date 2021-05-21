from django.db import models
from website.models import BaseField


class Prestation(BaseField):
    
    icon = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Prestation'
        verbose_name_plural = 'Prestations'

    def __str__(self):
        return self.title

class Category(BaseField):
    
    nom = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.nom

class Galery(BaseField):
    
    label= models.CharField(max_length=250)
    image = models.FileField(upload_to='images')
    category = models.ForeignKey("service.Category", verbose_name=("category_galery"), on_delete=models.CASCADE,related_name='categorygalery')

    class Meta:
        verbose_name = 'Galery'
        verbose_name_plural = 'Galerys'

    def __str__(self):
        return self.label


class Blog(BaseField):
    
    image = models.FileField(upload_to='images')
    title =  models.CharField(max_length=255 , blank=True , null=True )
    subtitle = models.CharField(max_length=250, blank=True , null=True)
    description = models.TextField(blank=True , null=True)
    image2 = models.FileField(upload_to='images', blank=True , null=True)
    title2 =  models.CharField(max_length=255, blank=True , null=True)
    subtitle2 = models.CharField(max_length=50, blank=True , null=True)
    description2 = models.TextField( blank=True , null=True)
    paragraph = models.TextField(blank=True , null=True)
  
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title


class Contact(BaseField):
    
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom


class Saison(BaseField):
    
    image = models.FileField( upload_to='images')
    nom = models.CharField(max_length=250)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Saison'
        verbose_name_plural = 'Saisons'

    def __str__(self):
        return self.nom


# Create your models here.
