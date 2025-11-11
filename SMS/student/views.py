from django.shortcuts import render, redirect
from student.models import Cred
from student.models import student as Stu

# Create your views here.
def landing(request):
    if request.method == 'POST':
        user = request.POST.get('uname')
        password = request.POST.get('password')

        res = Cred.objects.filter(
            uname = user,
            password = password).exists()
        if res:
            return redirect('home')
        else:
            return render(request, 'landing.html')
    else:
        return render(request, 'landing.html')
    
def home(request):
    return render(request, 'home.html')

def student(request):
    return render(request, 'student.html')

def stu_reg(request):
    if request.method == "POST":
        surname = request.POST.get('surname')
        lname = request.POST.get('lastname')
        gname = request.POST.get('guardname')
        mname = request.POST.gmet('mothername')
        cno = request.POST.get('cno')
        email = request.POST.get('email')
        addr = request.POST.get('address')
        cls = request.POST.get('class')
        
        roll_no = Stu.objects.filter(cls_name = cls).count()
        roll_no += 1

        Stu.objects.create(
            ssname = surname,
            slname = lname,
            gfname = gname,
            mname = mname,
            ph_no = cno,
            email = email,
            addr = addr,
            cls_name = cls,
            roll = roll_no
        )
        redirect('student')
    else:
        return render(request, 'stu_reg.html')