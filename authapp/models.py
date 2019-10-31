from django.db import models

# Create your models here.
class Register(models.Model):
    fname=models.CharField(max_length=20)
    phno=models.IntegerField()
    email=models.EmailField()
    uname=models.CharField(primary_key=True,max_length=20)
    pwd=models.CharField(max_length=15)
    cpwd=models.CharField(max_length=15)

