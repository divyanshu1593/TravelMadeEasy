from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Agent(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static',default=1)
    isRefundable = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    person = models.ManyToManyField(Person, blank=True, null=True)

class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=100)
    image =  models.ImageField(upload_to='static',default=1)
    number = models.CharField(max_length=100)
    rent = models.IntegerField(default=0)
    company = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    person = models.ManyToManyField(Person, blank=True, null=True)
