from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models, forms


# Create your views here.
#About us
def about(request):
    about = models.About_us.objects.all()
    return render(request, 'about.html', {'about':about})

#For contacts
def contact(request):
    contact = models.Contact.objects.all()
    return render(request, 'calling.html', {'contact': contact})

#For home
def home(request):
    home = models.Home.objects.all()
    return render(request, 'index.html', {'home': home})

def service(request):
    service = models.Service_content.objects.all()
    return render(request, 'service.html', {'service':service})

def add_form(request):
    method = request.method
    if method == "POST":
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'form_sended.html', {'form': form})

    else:
        form = forms.Form()
    return render(request, 'add_form.html', {'form': form})

def data_form(request):
    data = models.Form.objects.all()
    return render(request, 'form_data.html', {'data': data})

#For guides
def guides(request):
    guides = models.Guides.objects.all()
    return render(request, 'repair.html', {'guides' : guides})

