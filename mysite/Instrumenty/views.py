from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Rodzaj, Instrument, Muzyk 

class RodzajView(generic.ListView):
    template_name = 'rodzaj.html'
    context_object_name = 'rodzaj_list'

    def get_queryset(self):
        return Rodzaj.objects.all()


class InstrumentView(generic.ListView):
    context_object_name = 'instrument_list'
    template_name = 'instrument.html'
    
    def get_queryset(self):
        return Instrument.objects.all()

class MuzykView(generic.DetailView):
    model = Muzyk
    template_name = 'muzyk.html'