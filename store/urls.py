from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('project-details/<int:pk>', views.project_details, name="project-details"),  
    path('reserve/<int:pk>', views.reserve, name="reserve"),
    path('reserver/<int:pk>', views.reserver, name="reserver"),
    path('service/<int:pk>', views.view_service, name="service"),
    path('projects-details/<int:pk>', views.projects_details, name="projects-details"),
    
]
