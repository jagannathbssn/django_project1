from django.db import models

# Create your models here.
class Cred(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)

class student(models.Model):
    id = models.AutoField(primary_key=True)
    ssname = models.CharField(max_length=50, null=False)
    slname = models.CharField(max_length=200, null=False)
    gfname = models.CharField(max_length=200, null=False)
    mname = models.CharField(max_length=200)
    ph_no = models.BigIntegerField(unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    addr = models.CharField(max_length=400, null=False)
    cls_name = models.CharField(max_length=100, null=True)
    roll = models.IntegerField(null=False)
