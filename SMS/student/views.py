from django.shortcuts import render, redirect
from student.models import Cred

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