from django.db import models


# Create your models here.
# (3) creating model class to create form .

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

