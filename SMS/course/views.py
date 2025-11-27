from django.shortcuts import render
from course.models import Prog

# Create your views here.
def course(request):
    return render(request, 'course.html')

def cor_add_pro(request):
    if request.method == 'POST':
        pname = request.POST.get('pro_name')
        dur = request.POST.get('pro_dur')
        pdesc = request.POST.get('prog_desc')
        data = {}

        try:
            Prog.objects.create(pname = pname, dur = dur, pdesc = pdesc)
            data["msg1"] = "Academic Program Details, sucessfully added"
            data["val"] = 1
            data["msg2"] = "Please click the button below to return to the previous page."
            data["modu"] = "cor_add_pro"
        except Exception as e:
            data["msg1"] = "Operation unsucessful, please check the details"
            data["val"] = 0
            data["msg2"] = "Please click the button below to return to the previous page."
            data["modu"] = "cor_add_pro"
            data['err'] = e

    return render(request, 'message.html', data)

def cor_del_pro(request):
    return render(request, 'cor_del_pro.html')

def cor_add(request):
    return render(request, 'cor_add.html')

def cor_del(request):
    return render(request, 'cor_del.html')

def acs(request):
    return render(request, 'cor_ass.html')