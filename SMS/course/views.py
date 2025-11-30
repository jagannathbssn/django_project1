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
            data["msg2"] = "Please click the button below to return to the previous page."
            data["modu"] = "cor_add_pro"

            Prog.objects.create(pname = pname, dur = dur, pdesc = pdesc)
            data["msg1"] = "Academic Program Details, sucessfully added"
            data["val"] = 1

        except Exception as e:
            data["msg1"] = "Operation unsucessful, please check the details"
            data["val"] = 0
            data['err'] = e
            
        return render(request, 'message.html', data)
    return render(request, 'cor_add_pro.html')

def cor_del_pro(request):
    if request.method == 'POST':
        if request.POST.get('gpid'):
            pid = request.POST.get('gpid')
        if request.POST.get('gpname'):
            pname = request.POST.get('gpname')
        if request.POST.get('pro_name'):
            pid = request.POST.get('pro_id')
        return render(request, 'cor_del_pro.html')
    return render(request, 'cor_del_pro.html')

def cor_add(request):
    return render(request, 'cor_add.html')

def cor_del(request):
    return render(request, 'cor_del.html')

def acs(request):
    return render(request, 'cor_ass.html')