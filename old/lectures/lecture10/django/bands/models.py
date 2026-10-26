from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
