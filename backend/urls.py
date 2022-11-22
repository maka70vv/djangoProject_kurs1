from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),
    path('home/', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('form/', views.add_form, name='form'),
    path('form/postuser/', views.add_form, name='postuser'),
    path('database/', views.data_form, name='data'),
    path('guides/', views.guides, name='guides'),
]