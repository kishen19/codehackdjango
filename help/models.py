from django.db import models

class Person(models.Model):
    num = models.IntegerField()
    locationx = models.FloatField()
    locationy = models.FloatField()
