from django.db import models

class shelter(models.Model):
    name = models.CharField(max_length=250)
    x = models.FloatField()
    y = models.FloatField()
    address = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    supplyrequest = models.CharField(max_length=5000,default='Nothing!')