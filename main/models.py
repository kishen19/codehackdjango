from django.db import models

class hospital(models.Model):
    name = models.CharField(max_length=250)
    locationx = models.FloatField()
    locationy = models.FloatField()
    address = models.CharField(max_length=1000)