from django.contrib import admin
from . import models

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = ('title','creat_at','update_at','status')
    list_editable = ('status',)

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ('creat_at','update_at','status')
    list_editable = ('status',)


@admin.register(models.OptionAbout)
class OptionAboutAdmin(admin.ModelAdmin):

    list_display = ('creat_at','update_at','status')
    list_editable = ('status',)


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = ('nom','post','creat_at','update_at','status')
    list_editable = ('status',)

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('email','creat_at','update_at','status')
    list_editable = ('status',)

@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):

    list_display = ('lien','creat_at','update_at','status')
    list_editable = ('status',)

@admin.register(models.WebSite)
class WebSiteAdmin(admin.ModelAdmin):

    list_display = ('nom_site','creat_at','update_at','status')
    list_editable = ('status',)




# Register your models here.


