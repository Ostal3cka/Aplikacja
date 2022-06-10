from django.shortcuts import render
from django.http import HttpResponse 
from .models import Rodzaje, Instruments, Muzycy
from .forms import Form
from django.template import loader


def index(request):
    index_list = 'Rodzaj', 'Instrument', 'Muzyk', 'Form'
    template = loader.get_template('instrumenty/index.html')
    context = {
        'index_list': index_list,
    }
    return HttpResponse(template.render(context, request))

def Rodzaj(request):
    rodzaj_list = Rodzajs.objects.all
    template = loader.get_template('instrumenty/Rodzaj.html')
    context = {
        'rodzaj_list': rodzaj_list,
    }
    return HttpResponse(template.render(context, request))

def Instrument(request):
    instrument_list = Instrument.objects.all
    template = loader.get_template('instrumenty/Instrument.html')
    context = {
        'instrument_list': instrument_list,
    }
    return HttpResponse(template.render(context, request))

def Muzyk(request):
    muzyk_list = Muzyk.objects.all
    template = loader.get_template('instrumenty/Muzyk.html')
    context = {
        'muzyk_list': muzyk_list,
    }
    return HttpResponse(template.render(context, request))

def form(request):
    form_list= Form()
    context = {
        'form_list': form_list
    }
    return render(request,'instrumenty/form.html', context)

