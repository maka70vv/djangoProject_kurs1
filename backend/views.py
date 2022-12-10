from django.forms import forms
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models, forms
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "login_success.html", {"form": form})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# Create your views here.
# About us page
def about(request):
    about = models.About_us.objects.all()
    return render(request, "about.html", {"about": about})


# For contact page
def contact(request):
    contact = models.Contact.objects.all()
    return render(request, "calling.html", {"contact": contact})


# For main page
def home(request):
    home = models.Home.objects.all()
    return render(request, "index.html", {"home": home})


def service(request):
    service = models.Service_content.objects.all()
    return render(request, "service.html", {"service": service})


def add_form(request):
    method = request.method
    if method == "POST":
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "form_sended.html", {"form": form})

    else:
        form = forms.Form()
    return render(request, "add_form.html", {"form": form})


class Data_form(generic.ListView):
    template_name = "form_data.html"
    queryset = models.Form.objects.all()

    def get_queryset(self):
        return models.Form.objects.all()


class DataDetailView(generic.DetailView):
    template_name = "details.html"

    def get_object(self, **kwargs):
        data_id = self.kwargs.get("id")
        return get_object_or_404(models.Form, id=data_id)


class DataDeleteView(generic.DeleteView):
    template_name = "delete.html"
    success_url = "/database/"

    def get_object(self, **kwargs):
        data_id = self.kwargs.get("id")
        return get_object_or_404(models.Form, id=data_id)


# For guides
def guides(request):
    guides = models.Guides.objects.all()
    return render(request, "repair.html", {"guides": guides})
