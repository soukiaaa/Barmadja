from django import forms
from . import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model=models.client
        fields=['name','phone','isregistred','project']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.customer
        fields=['name','phone','service','description']