from django import forms
from . import models

class Form(forms.ModelForm):
    class Meta:
        model = models.Form
        fields = '__all__'
