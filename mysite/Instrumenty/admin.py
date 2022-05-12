from django.contrib import admin

# Register your models here.
from .models import Instrument, Muzyk, Rodzaj

admin.site.register(Instrument)
admin.site.register(Muzyk)
admin.site.register(Rodzaj)


