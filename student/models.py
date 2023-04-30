from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique= True)
    country = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField( max_length=254, unique=True, null= False)
    password = models.CharField(max_length=50)