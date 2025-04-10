from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars

# Create your models here.
class service(models.Model):
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-designation']
    def __str__(self):
        return self.designation  
    
class category(models.Model):
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['-designation']
    def __str__(self):
        return self.designation 

class project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=200)
    services = models.ForeignKey(category, on_delete=models.PROTECT) 
    srv = models.ForeignKey(service, on_delete=models.PROTECT) 

    class Meta:
        ordering = ['-title']
    def __str__(self):
        return self.title  
    
class projects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=200) 
    price = models.FloatField() 
    nbrView = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['-title']
    def __str__(self):
        return self.title 

class comment(models.Model):
    datec = models.DateTimeField(auto_now_add=True)
    proj = models.ForeignKey(projects, on_delete=models.CASCADE) 
    content = models.TextField()

    def __str__(self):
        return self.content 
    
class client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    isregistred = models.BooleanField(default=False)
    project = models.ForeignKey(project, on_delete=models.PROTECT) 
    datec = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']  

    def __str__(self):
        return self.name
    def __int__(self):
        return self.name
    
TYPE_CHOICE = (
    ('Etudiant','Etudiant'),
    ('Formateur', 'Formateur'),
    ('Développeur', 'Développeur'),
    ('Demandeur', 'Demandeur'),
    ('Autre','Autre'),
)

class customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(service, on_delete=models.PROTECT)
    type = models.CharField(max_length=50, choices=TYPE_CHOICE, default='Etudiant')
    datec = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['-name']  
    def __str__(self):
        return self.name
    def __int__(self):
        return self.name
    
class customerPrj(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    prj = models.ForeignKey(projects, on_delete=models.PROTECT) 
    datec = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['-name']  
    def __str__(self):
        return self.name
    def __int__(self):
        return self.name
    

TYPE_CHOICES = (
    ('simple','simple'),
    ('intermediate', 'intermediate'),
    ('professionnel','professionnel'),
)

TYPE_STATUS = (
    ('not yet', 'not yet'),
    ('in progress','in progress'),
    ('done','done'),
)

class sales(models.Model):
    prix = models.FloatField()
    etat = models.CharField(max_length=50, choices=TYPE_STATUS, default='not yet')
    duree = models.CharField(max_length=20)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='pose')
    dated = models.DateField()
    datef = models.DateField()
    payer = models.CharField(max_length=20)
    client = models.ForeignKey(client, on_delete=models.PROTECT) 
    project = models.ForeignKey(project, on_delete=models.PROTECT) 
    class Meta:
        ordering = ['-etat']  

    def __str__(self):
        return self.etat
    def __int__(self):
        return self.id
    
class payment(models.Model):
    montant = models.FloatField()
    versement_date_time = models.DateTimeField(auto_now_add=True)
    sales = models.ForeignKey(sales, on_delete=models.PROTECT)
    class Meta:
        ordering = ['-sales']  

    def __str__(self):
        return self.sales.id
    
