from django.db import models
from django_resized import ResizedImageField
import os
from datetime import datetime

# Create your models here.
class Cred(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=21, null=False)

def rename_student_photo(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.sid}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    return os.path.join("student_photos", new_filename)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    sfname = models.CharField(max_length=100, null=False)
    smname = models.CharField(max_length=200, null=True, blank=True)
    slname = models.CharField(max_length=100, null=False)
    gfname = models.CharField(max_length=100, null=False)
    mname = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=False)
    gend = models.CharField(max_length=10, null=False)
    gc_no = models.BigIntegerField(null=False)  
    ph_no = models.BigIntegerField(null=False)
    email = models.CharField(max_length=200, null=False, unique=True)
    location = models.CharField(max_length=200, null=False)
    addr = models.TextField()
    prog = models.CharField(max_length=150, null=False)
    year = models.IntegerField(null=False)
    sem = models.IntegerField(null=False)
    cls_name = models.CharField(max_length=100, null=False)
    roll = models.IntegerField(null=False)
    sid = models.CharField(max_length=200, null=False, unique=True)
    joining_date = models.DateField(null=False)
    relieving_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, null=False, default="Active")
    photo = ResizedImageField(
        size=[500, 500],
        upload_to=rename_student_photo,
        force_format="JPEG" 
    )

class Del_users(models.Model):
    sid = models.CharField(max_length=200, null=False, unique=True)
    details = models.TextField(null=False)
    time = models.DateTimeField(null=False)
    