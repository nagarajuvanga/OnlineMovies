
from django.db import models

class Movietable(models.Model):
    moviename=models.CharField(max_length=50,unique=True)
    t_ype=models.CharField(max_length=30)
    rank=models.IntegerField()
    casting=models.CharField(max_length=50)
    release=models.IntegerField()
    image=models.ImageField(upload_to='image/')

class Usersignuptable(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()
    username=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)

class Userlogintable(models.Model):
    usrname=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)
