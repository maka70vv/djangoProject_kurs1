from django import forms
from . import models


class Form(forms.ModelForm):
    class Meta:
        model = models.Form
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
