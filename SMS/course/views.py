from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request, 'course.html')

def cor_add_pro(request):
    return render(request, 'cor_add_pro.html')

def cor_del_pro(request):
    return render(request, 'cor_del_pro.html')

def cor_add(request):
    return render(request, 'cor_add.html')

def cor_del(request):
    return render(request, 'cor_del.html')

def acs(request):
    return render(request, 'cor_ass.html')