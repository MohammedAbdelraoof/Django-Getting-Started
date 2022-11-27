from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    
    def __str__(self):
        return f"Product name: {self.name}"
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return f"User name: {self.name}"