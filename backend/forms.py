from django import forms
from . import models


#Calling form
class Form(forms.ModelForm):
    class Meta:
        model = models.Form
        fields = "__all__"


#Login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
