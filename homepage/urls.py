from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('help', views.help, name='help'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
]
