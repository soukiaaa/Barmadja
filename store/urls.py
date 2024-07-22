from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('about', views.about, name="about"),
    path('project-details/<int:pk>', views.project_details, name="project-details"),  
    path('reserve/<int:pk>', views.reserve, name="reserve"),
      
]
