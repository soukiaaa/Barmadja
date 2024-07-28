from django.shortcuts import render,redirect
from . models import *
from . import forms
from django.contrib import messages

# Create your views here.
def store(request):
	services = service.objects.all()
	categories = category.objects.all()
	projects = project.objects.all()
	return render(request, 'index.html', {'services':services, 'categories':categories, 'projects':projects})

def about(request):
    context = {}
    return render(request, 'about.html', context)

def project_details(request,pk):
    projects=project.objects.get(id=pk)
    categorie=category.objects.get(designation=projects.service)
    return render(request, 'project-details.html', {'projects':projects, 'categorie':categorie})

def reserve(request,pk):
    projects=project.objects.get(id=pk)
    return render(request, 'reserve.html', {'projects':projects})

def reserver(request,pk):
    # projects=project.objects.get(id=pk)
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
    return render(request, 'view_service.html', {'vservices':services})