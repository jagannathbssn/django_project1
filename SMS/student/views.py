from django.shortcuts import render, redirect
from student.models import Cred
from student.models import Student as Stu
from course.models import Prog
from datetime import date as d

# Create your views here.
def landing(request):
    if request.method == 'POST':
        user = request.POST.get('uname')
        pas = request.POST.get('password')
        try:
            res = Cred.objects.get(uname = user, password = pas)
            if res:
                return redirect('home')
        except:
            msg = "please check the credentials"
            return render(request, 'landing.html', {"msg" : msg})
    return render(request, 'landing.html')

def message(request):
    return render(request, 'message.html')

def home(request):
    return render(request, 'home.html')

def student(request):
    return render(request, 'student.html')

def stu_reg(request):

    if request.method == 'POST':
        sur = request.POST.get('ssname')
        mid = request.POST.get('smname')
        last = request.POST.get('slname')
        gfname = request.POST.get('fgname')
        mname = request.POST.get('mname')
        dob = request.POST.get('dob')
        gend = request.POST.get('gender')
        gpno = request.POST.get('gpno')
        cno = request.POST.get('cno')
        email = request.POST.get('email')
        loc = request.POST.get('loca')
        addr = request.POST.get('addr')
        prog = request.POST.get('prog')
        dur = request.POST.get('dura')
        sem = request.POST.get('sem')
        cls_name = request.POST.get('cls')
        photo = request.FILES.get('photo')

        te = d.today()
        jdate = te

        try:

            roll = Stu.objects.filter(year = dur, cls_name = cls_name).count()
            roll += 101

            tp = Prog.objects.get(pname = prog)
            tc = Stu.objects.filter(prog = prog, year = dur).count()
            tc += 10001


            s = f"{d.today().year+int(dur)-1}{(tp.pid + 100)}{hex(tc)[2:]}"

            Stu.objects.create(
                sfname = sur,
                smname = mid,
                slname = last,
                gfname = gfname,
                mname = mname,
                dob = dob,
                gend = gend,
                gc_no = gpno,
                ph_no = cno,
                email = email,
                location = loc,
                addr = addr,
                prog = prog,
                year = dur,
                sem = sem,
                cls_name = cls_name,
                roll = roll,
                sid = s,
                joining_date = jdate,
                photo = photo,
            )

            data = {
                "msg1" : "Student registration is sucessful",
                "val" : 1,
                "msg2" : "Please click the button below to return to the previous page.",
                "modu" : "stu_reg"
            }
        except Exception as e:
            data = {

                "msg1" : "Student registration is Unsucessful, Please check the details",
                "val" : 0,
                "msg2" : "Please click the button below to return to the previous page.",
                "modu" : "stu_reg",
                "err" : e
            }
        
        return render(request, 'message.html', data)
    else:
        res = Prog.objects.values('pname')
        return render(request, "stu_reg.html", {"data" : res})
    
def stu_up(request):
    prog_names = Prog.objects.values("pname")
    class_names = Stu.objects.values("cls_name").distinct()
    data = {
        "prog_name" : prog_names,
        "class_name" : class_names
    }
    if request.method == "POST":

        if request.POST.get('ssname'):
            ssname = request.POST.get('ssname')
            smname = request.POST.get('smname')
            slname = request.POST.get('slname')
            fgname = request.POST.get('fgname')
            nmname = request.POST.get('nmname')
            dob = request.POST.get('dob')
            gen = request.POST.get('gender')
            gpno = request.POST.get('gpno')
            cno = request.POST.get('cno')
            email = request.POST.get('email')
            loca = request.POST.get('loca')
            addr = request.POST.get('addr')
            prog = request.POST.get('prog')
            dura = request.POST.get('dura')
            sem = request.POST.get('sem')
            cls = request.POST.get('cls')
            status = request.POST.get('status')

            sid1 = request.POST.get('student_id')
            photo = request.FILES.get('photo')

            try:
                res = Stu.objects.get(sid = sid1)
                res.sfname = ssname
                res.smname = smname
                res.slname = slname
                res.gfname = fgname
                res.mname = nmname
                res.dob = dob
                res.gend = gen
                res.gc_no = gpno
                res.ph_no = cno
                res.email = email
                res.location = loca
                res.addr = addr
                
                
                if cls != res.cls_name or prog != res.prog or dura != res.year or sem != res.sem:
                    te = Stu.objects.filter(prog = prog, year = dura, sem = sem, cls_name = cls).count()
                    te += 1
                    res.roll = te

                res.prog = prog
                res.year = dura
                res.sem = sem
                res.cls_name = cls

                if status == "Relieved":
                    res.relieving_date = d.today()

                res.status = status

                
                if photo:
                    res.photo.delete(save=False)
                    res.photo = photo

                res.save()

                data["msg1"] = "Updating student details is sucessful"
                data["val"] = 1
                data["msg2"] = "Please click the button below to return to the previous page."
                data["modu"] = "stu_up"

            except Exception as e:
                    data["msg1"] = "Updating student details is not sucessful, Please check the details"
                    data["val" ] = 0
                    data["msg2"] = "Please click the button below to return to the previous page."
                    data["modu"] = "stu_up"
                    data["err" ] = e  
            return render(request, 'message.html', data)
            
        else:
            try:
                if request.POST.get('sid'):
                    sid = request.POST.get('sid')
                    sobj = Stu.objects.get(sid = sid)
                    data["sobj"] = sobj
                elif request.POST.get('seid'):
                    em = request.POST.get('seid')
                    sobj = Stu.objects.get(email = em)
                    data["sobj"] = sobj
                elif request.POST.get('spro'):
                    pro = request.POST.get('spro')
                    year = request.POST.get('syear')
                    ssem = request.POST.get('ssem')
                    scls = request.POST.get('scls')
                    rol = request.POST.get('sroll')
                    sobj = Stu.objects.get(
                        prog = pro,
                        year = year,
                        sem = ssem,
                        cls_name = scls,
                        roll = rol)
                    data["sobj"] = sobj
            except Exception as e:
                data["msg1"] = "Updating student details is not sucessful, Please check the details"
                data["val" ] = 0
                data["msg2"] = "Please click the button below to return to the previous page."
                data["modu"] = "stu_up"
                data["err" ] = e
                return render(request, "message.html", data)
        return render(request, "stu_up.html", data)
    else:
        return render(request, "stu_up.html", data)
    
def stu_del(request):
    return render(request, 'stu_del.html')
