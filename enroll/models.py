from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100,null=True)
    pan=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)