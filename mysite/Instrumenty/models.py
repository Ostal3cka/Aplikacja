from django.db import models

# Create your models here.
class Rodzaj(models.Model):
    nazwa = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nazwa

class Instrument(models.Model):
    nazwa = models.CharField(max_length=200, null=True)
    opis = models.CharField(max_length=500, null=True)
    rodzaj = models.ForeignKey(Rodzaj, on_delete=models.CASCADE, null=True)
    muzyk = models.ManyToManyField("Muzyk")

    def __str__(self):
        return self.nazwa

class Muzyk(models.Model):
    nazwa = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nazwa



