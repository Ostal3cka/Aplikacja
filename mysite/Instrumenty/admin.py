from django.contrib import admin

# Register your models here.
from .models import Instruments, Muzycy, Rodzaje

admin.site.register(Instruments)
admin.site.register(Muzycy)
admin.site.register(Rodzaje)


