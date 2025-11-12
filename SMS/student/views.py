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
        mname = request.POST.get('mothername')
        date = request.POST.get('dob')
        gender = request.POST.get('gender')
        cno = request.POST.get('cno')
        email = request.POST.get('email')
        addr = request.POST.get('address')
        cls = request.POST.get('class')
        
        roll_no = Stu.objects.filter(cls_name = cls).count()
        roll_no += 1

        try:
            Stu.objects.create(
            ssname = surname,
            slname = lname,
            gfname = gname,
            mname = mname,
            dob = date,
            gender = gender,
            ph_no = cno,
            email = email,
            addr = addr,
            cls_name = cls,
            roll = roll_no
            )
            msg = "You operation is sucessful"
        except:
            msg = "Your operation is unsucessful"
        return render(request, 'message.html', {'data' : {'msg' : msg}})
    else:
        return render(request, 'stu_reg.html')
    
def stu_up(request):
    if request.method == 'POST':
        classname = request.POST.get('cls')
        rollno = request.POST.get('roll')
        try:
            person = Stu.objects.get(cls_name = classname, roll = rollno)
            return render(request, 'update.html', {"data" : person})
        except:
            msg = "Please, check the details again"
            return render(request, 'message.html', {'data': {'msg' : msg}})
    res = Stu.objects.values('cls_name').order_by('cls_name').distinct
    return render(request, 'stu_up.html', {'data' : res})

def updating(request):
    return render(request, 'home.html')