from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rodzaj/', views.Rodzaj, name='Rodzaj'),
    path('instrument/', views.Instrument, name='Instrument'),
    path('muzyk/', views.Muzyk, name='Muzyk'),
    path('form/', views.form, name='form') 
    ]