from pyexpat import model
from django.db import models

# Create your models here.
class EntryModels(models.Model):
    
    datetime = models.DateTimeField()
    concept = models.CharField(max_length=255)
    amount = models.FloatField()