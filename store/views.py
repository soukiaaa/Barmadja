from django.shortcuts import render,redirect
from . models import *
from . import forms
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
def store(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,)
        messages.success(request, 'Votre message a été bien transmis')
    services = service.objects.all()
    categories = category.objects.all()
    projets = project.objects.all()
    projectss = projects.objects.all()
    return render(request, 'index.html', {'services':services, 'categories':categories, 'projects':projets, 'proj':projectss})

def about(request):
    context = {}
    return render(request, 'about.html', context)

def project_details(request,pk):
    projects=project.objects.get(id=pk)
    categorie=category.objects.get(designation=projects.services)
    return render(request, 'project-details.html', {'projects':projects, 'categorie':categorie})

def reserve(request,pk):
    projects=project.objects.get(id=pk)
    return render(request, 'reserve.html', {'projects':projects})

def reserver(request,pk):
    registerForm=forms.RegisterForm()
    registerForm.fields["project"].initial = pk
    if request.method=='POST':
        registerForm=forms.RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'تم التسجيل بنجاح')
            return redirect('store') 
        else:
             messages.success(request, 'لم يتم التسجيل بنجاح')
    return render(request, 'login2022end/index.html', {'registerForm':registerForm})

def view_service(request,pk):
    services=service.objects.get(id=pk)
    serviceForm = forms.CustomerForm()
    serviceForm.fields["service"].initial = pk
    if request.method=='POST':
        serviceForm=forms.CustomerForm(request.POST)
        if serviceForm.is_valid():
            serviceForm.save()
            messages.success(request, 'تم التسجيل بنجاح')
            return redirect('store') 
        else:
             messages.success(request, 'لم يتم التسجيل بنجاح')
    return render(request, 'view_service.html', {'vservices':services,'serviceForm':serviceForm})
