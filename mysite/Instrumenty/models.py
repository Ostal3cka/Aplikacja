from django.db import models

# Create your models here.
class Rodzaje(models.Model):
    nazwa = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nazwa

class Instruments(models.Model):
    nazwa = models.CharField(max_length=200, null=True)
    opis = models.CharField(max_length=500, null=True)
    rodzaj = models.ForeignKey(Rodzaje, on_delete=models.CASCADE, null=True)
    muzyk = models.ManyToManyField("Muzycy")

    def __str__(self):
        return self.nazwa

class Muzycy(models.Model):
    nazwa = models.CharField(max_length=200, null=True)
    opis = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.nazwa



