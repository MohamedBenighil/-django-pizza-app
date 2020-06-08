from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10) 