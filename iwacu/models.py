from django.db import models

# Create your models here.

class Herbals(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField()

class Imigani(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Sakwe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    answer = models.TextField()

class Amateka(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

class Diy(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField()
    description = models.TextField()

class Customer(models.Model):
    address = models.CharField(max_length=255)
    names = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,default="male")
    National_id = models.IntegerField(max_length=255)
    phonenumber = models.CharField(max_length=255, default="947587986")

    