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
from course import views as v2
from marks import views as v3
from attendance import views as v4


from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.landing, name='landing'),
    path('home/', v1.home, name='home'),
    path('message/', v1.message, name='message'),

    path('student/', v1.student, name='student'),
    path('student/student-resgistration/', v1.stu_reg, name='stu_reg'),
    path('student/student-updation/', v1.stu_up, name='stu_up'),
    path('student/student-deletion/', v1.stu_del, name='stu_del'),
    path('student/student-profile/', v1.student, name='stu_pro'),


    path('course/', v2.course , name='course'),
    path('course/add-new-program', v2.cor_add_pro, name='cor_add_pro'),
    path('course/add-new-course', v2.cor_add, name="cor_add"),
    path('course/delete-program', v2.cor_del_pro, name='cor_del_pro'),
    path('course/delete-course', v2.cor_del, name='cor_del'),
    path('course/add-course-to-students', v2.acs, name='acs'),

    path('marks/', v3.marks, name='marks'),
    path('attendance/', v4.attendance, name='attendance'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)