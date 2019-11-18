from django.db import models

# Create your models here.
from django.db import models
class zainteresowania_uzytkownika(models.Model):
ID_zainteresowania = models.IntegerField()
Zainteresowanie = models.CharField(max_length=45)
ID_uzytkownika = models.IntegerField()
class Dane_uzytkownika(models.Model):
ID_uzytkownika = models.PrimaryKey(zainteresowania_uzytkownika, on_delete=models.primary)
Imie_uzytkownika = models.CharField(max_length=200)
Wiek = models.IntegerField()
Miejscowosc = models.CharField(max_length=45)
email = models.CharField(max_length=45)

models.DateField()
