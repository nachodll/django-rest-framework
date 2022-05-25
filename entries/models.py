from pyexpat import model
from django.db import models

# Create your models here.
class Entry(models.Model):
    
    datetime = models.DateTimeField()
    concept = models.CharField(max_length=255)
    amount = models.FloatField()
    
    def __str__(self) -> str:
        return f"Fecha y hora: {self.datetime} - Concepto: {self.concept} - Cantidad: {self.amount}"