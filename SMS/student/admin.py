from django.contrib import admin
from student.models import Cred, student, del_user

# Register your models here.
admin.site.register(Cred)
admin.site.register(student)
admin.site.register(del_user)