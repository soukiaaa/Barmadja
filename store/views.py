from django.shortcuts import render
from . models import *

# Create your views here.
def store(request):
	services = service.objects.all()
	projects = project.objects.all()
	return render(request, 'index.html', {'services':services,'projects':projects})

def about(request):
    context = {}
    return render(request, 'about.html', context)

def project_details(request,pk):
    projects=project.objects.get(id=pk)
    return render(request, 'project-details.html', {'projects':projects})