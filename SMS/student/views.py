from django.shortcuts import render, redirect
from student.models import Cred
from student.models import student as Stu
from student.models import del_user as Del

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
            msg = "Student Registration is sucessful"
    
        except:
            msg = "Student Registration is unsucessful"
        
        data = {
                "msg1" : msg,
                "msg2" : "Please click the below button to go to previous page",
                "modu" : "student"
            }
        return render(request, 'message.html', data)
    else:
        return render(request, 'stu_reg.html')
    
def stu_up(request):
    if request.method == 'POST':
        if request.POST.get('roll'):
            classname = request.POST.get('cls')
            rollno = request.POST.get('roll')
            try:
                person = Stu.objects.get(cls_name = classname, roll = rollno)
                return render(request, 'update.html', {"data" : person})
            except:
                data = {
                "msg1" : "Please, check the details again",
                "msg2" : "Please click the below button to go to previous page",
                "modu" : "student"
                }
                return render(request, 'message.html', data)
        else:
            a1 = request.POST.get('surname1')
            a2 = request.POST.get('lastname1')
            a3 = request.POST.get('guardname1')
            a4 = request.POST.get('mothername1')
            a5 = request.POST.get('dob1')
            a6 = request.POST.get('gender')
            a7 = request.POST.get('cno1')
            a8 = request.POST.get('email1')
            a9 = request.POST.get('address1')
            a10 = request.POST.get('class1')
            a11 = request.POST.get('scn')
            a12 = request.POST.get('sid')

            try:
                res = Stu.objects.get(id = a12)

                res.ssname = a1
                res.slname = a2
                res.gfname = a3
                res.mname = a4
                res.dob = a5
                res.gender = a6
                res.ph_no = a7
                res.email = a8
                res.addr = a9

                if a10 == a11:
                    res.save()
                else:
                    count = Stu.objects.filter(cls_name = a10).count()
                    res.roll = count + 1
                    res.cls_name = a10
                    res.save()
                
                data = {
                    "msg1" : "The update operation is sucessful",
                    "msg2" : "Please click the below button to go to previous page",
                    "modu" : "student"
                }

                
            except:
                data = {
                    "msg1" : "The update operation is unsucessful, please check the detalis",
                    "msg2" : "Please click the below button to go to previous page",
                    "modu" : "student"
                }

            return render(request, 'message.html', data)

    else:
        res = Stu.objects.values('cls_name').order_by('cls_name').distinct
        return render(request, 'stu_up.html', {'data' : res})
    
def stu_del(request):
    if request.method == 'POST':
        if request.POST.get('roll'):
            classname = request.POST.get('cls')
            roll = request.POST.get('roll')
            
            try:
                obj = Stu.objects.get(cls_name = classname, roll = roll)
                return render(request, 'deleting.html', {'data' : obj})
            except:
                data = {
                    "msg1" : "please check the details",
                    "msg2" : "please click the button to return to previous page",
                    "modu" : "student"
                }
                return render(request, 'message.html', data)
        else:
            sid = request.POST.get('sid')
            
            try:
                obj = Stu.objects.get(id = sid)
            
                sname = obj.ssname + obj.slname
                scno = obj.ph_no
            
                Del.objects.create(sid = sid, name = sname, ph_no = scno)
                obj.delete()

                data = {
                    "msg1" : "the data is sucessfully deleted",
                    "msg2" : "please click the button to return to previous page",
                    "modu" : "student"
                }
            except:
                data = {
                    "msg1" : "operations is unsucessfully please try again",
                    "msg2" : "please click the button to return to previous page",
                    "modu" : "student"
                }

                return render(request, 'message.html', data)

            return render(request, 'message.html', data)
        
    else:
        res = Stu.objects.values('cls_name').order_by('cls_name').distinct
        return render(request, 'stu_del.html', {'data' : res})
