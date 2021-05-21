from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class BaseField(models.Model):

    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default = True)

    class Meta:
        abstract = True

class Banner(BaseField):
    
    image = models.FileField(upload_to='images')
    label = models.CharField(max_length=50)
    description = models.TextField()
    title = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title


class About(BaseField):
    
    image = models.FileField(upload_to='images')
    option = models.ManyToManyField("website.OptionAbout", verbose_name=("option_about"), related_name='optionabout')
    lien = models.URLField(max_length=200)
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class OptionAbout(BaseField):
    
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'OptionAbout'
        verbose_name_plural = 'OptionAbouts'

    def __str__(self):
        return self.name
    

class Testimonial(BaseField):
    
    image = models.FileField(upload_to='images')
    nom = models.CharField(max_length=50)
    message = models.TextField()
    post = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.nom


class Newsletter(BaseField):
    
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email


class Sociaux(BaseField):
    
    icon = models.CharField(max_length=255)
    lien = models.URLField(max_length=200)
    
    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'sociaux'

    def __str__(self):
        return self.lien


class WebSite(BaseField):
    
    nom_site = models.CharField(max_length=255)
    description_about = models.TextField()
    description_contact = models.TextField()
    description_service = models.TextField()
    title_contact = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    adresse =models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)

    
    class Meta:
        verbose_name = 'WebSite'
        verbose_name_plural = 'WebSites'

    def __str__(self):
        return self.nom_site