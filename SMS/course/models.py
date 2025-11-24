from django.db import models

# Create your models here.
class Prog(models.Model):

    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=200, null=False, unique=True)
    dur = models.IntegerField(null=False)
    pdesc = models.TextField(null=False)

class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    pid = models.IntegerField(null=False)
    pname = models.CharField(max_length=200, null=False)
    cname = models.CharField(max_length=200, null=False)
    tname = models.CharField(max_length=200, null=False)
    dur = models.IntegerField(null=False)
    desc1 = models.TextField(null=False)
    