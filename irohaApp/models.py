from django.db import models

# Create your models here.
class produto(models.Model):
    id=models.CharField(max_length=255,primary_key=True) 
    nome=models.CharField(max_length=50)
    status=models.CharField( max_length=50)
