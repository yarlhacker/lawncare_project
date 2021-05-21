from django.shortcuts import get_object_or_404, render,redirect
from . import models
from service import models as models_service
from django.contrib import messages


def newletter(request):
    
    newletter = request.POST.get('email')
    models.Newsletter.objects.create(email = newletter) # Pour enegister dans la base de donner
    retour = request.META.get('HTTP_REFERER')# Pour rediriger sur la meme page
    return redirect(retour,'/')

def index(request):
    banners = models.Banner.objects.filter(status=True)
    prestations = models_service.Prestation.objects.filter(status=True)
    about =  models.About.objects.filter(status=True).first()
    aboutoptions =models.OptionAbout.objects.filter(status=True)
    saisons = models_service.Saison.objects.filter(status=True)
    testimonials = models.Testimonial.objects.filter(status=True)
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    blogs = models_service.Blog.objects.filter(status=True).order_by('-creat_at')[:3]
    return render(request,'index.html',locals())

def about(request):
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    return render(request,'about.html',locals())

def blog_single(request,id):
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    blogs = models_service.Blog.objects.filter(status=True).order_by('-creat_at')[:3]
    blog = get_object_or_404(models_service.Blog, id=id)
    prestations = models_service.Prestation.objects.filter(status=True)
    return render(request,'blog-single.html',locals())

def blog(request):
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    blogs = models_service.Blog.objects.filter(status=True)
    return render(request,'blog.html',locals())

def gallery(request):
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    gallerys = models_service.Galery.objects.filter(status=True)
    return render(request,'gallery.html',locals())

def contact(request):
    abouts =  models.About.objects.filter(status=True)
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    if request.method == 'POST':
        
        new_contact = models_service.Contact(
            nom = request.POST['name'],
            email = request.POST['email'],
            sujet =request.POST['subject'],
            message = request.POST['message']
        )
        new_contact.save()
        messages.success(request, 'message envoye')
        return redirect('contact')
        
    return render(request,'contact.html',locals())

def service(request):
    websites = models.WebSite.objects.filter(status=True)
    sociaux = models.Sociaux.objects.filter(status=True)
    return render(request,'services.html',locals())
# Create your views here.
