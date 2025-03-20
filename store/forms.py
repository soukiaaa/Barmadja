from django import forms
from . import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model=models.client
        fields=['name','phone','isregistred','project']

class CustomerForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
    }))
    class Meta:
        model=models.customer
        fields=['name','phone','service','type','description']
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'اترك تعليق',
        'rows': '2',
    }))
    class Meta:
        model=models.comment
        fields=['content','proj']

class CustumProjectForm(forms.ModelForm):
   
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'الوصف',
        'rows': '2',
    }))
    class Meta:
        model=models.customerPrj
        fields=['name','phone','description','prj']