from django.contrib import admin
from student.models import Cred
from student.models import Student as Stu

# Register your models here.
admin.site.register(Cred)
admin.site.register(Stu)