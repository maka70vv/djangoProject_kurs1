from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contacts/", views.contact, name="contacts"),
    path("", views.home, name="home"),
    path("service/", views.service, name="service"),
    path("form/", views.add_form, name="form"),
    path("form/postuser/", views.add_form, name="postuser"),
    path("database/", views.Data_form.as_view(), name="data"),
    path("database/<int:id>/", views.DataDetailView.as_view(), name="show_detail"),
    path("login/", views.user_login, name="login"),
    path("guides/", views.guides, name="guides"),
]
