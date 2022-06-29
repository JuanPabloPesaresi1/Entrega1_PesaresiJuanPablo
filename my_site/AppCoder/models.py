import email
from django.db import models

# Create your models here.

class Familiares(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fechaDeNacimiento=models.IntegerField()
    email=models.EmailField(blank=True,null=True)