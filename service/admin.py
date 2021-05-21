from django.contrib import admin
from . import models

@admin.register(models.Prestation)
class PrestationAdmin(admin.ModelAdmin):
	list_display = ('title','creat_at','update_at','status',)
	list_editable = ('status',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('nom','creat_at','update_at','status',)
    list_editable = ('status',)


@admin.register(models.Galery)
class GaleryAdmin(admin.ModelAdmin):

    list_display = ('label','creat_at','update_at','status',)
    list_editable = ('status',)


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('subtitle','creat_at','update_at','status',)
    list_editable = ('status',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('nom','email','creat_at','update_at','status',)
    list_editable = ('status',)

@admin.register(models.Saison)
class SaisonAdmin(admin.ModelAdmin):

    list_display = ('nom','creat_at','update_at','status',)
    list_editable = ('status',)



