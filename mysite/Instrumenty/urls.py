from django.urls import path
from . import views


urlpatterns = [
    path('rodzaj', views.Rodzaj.as_view(), name='rodzaj'),
    path('<instrument', views.Instrument.as_view(), name='instrument'),
    path('muzyk', views.Muzyk.as_view(), name='muzyk'),
    ]