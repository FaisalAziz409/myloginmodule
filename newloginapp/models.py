from django.db import models

# Create your models here
class Signup(models.Model):
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    address1=models.CharField(max_length=255)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip=models.IntegerField()


    def __str__(self):
        return self.email



class Weather(models.Model):
    city = models.CharField(max_length=110)

    def __str__(self):
        return self.city

