# Create your models here.
from django.db import models


class Temperature(models.Model):
    captime = models.DateTimeField(auto_now_add=False)
    captemperature = models.CharField(max_length=10)
    caphumidity = models.CharField(max_length=10)
    capillumination = models.CharField(max_length=10, default=99)
    capsoilmoisture = models.CharField(max_length=10, default=99)

    def __str__(self):
        return self.captemperature