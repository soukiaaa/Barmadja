from django import forms
from . import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model=models.client
        fields=['name','phone','isregistred','project']