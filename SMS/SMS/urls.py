"""
URL configuration for SMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views as v1
from attendance import views as v2
from course import views as v3
from marks import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.landing, name='landing'),
    path('home/', v1.home, name='home'),
    path('student/', v1.student, name='student'),

    path('student/student-registration/', v1.stu_reg , name='stu_reg'),
    path('student/updating-student-details/', v1.stu_up , name='stu_up'),

    path('attendance/', v2.attendance, name='attendance'),  
    path('course/', v3.course, name='course'),
    path('marks/', v4.marks, name='marks'),
]
