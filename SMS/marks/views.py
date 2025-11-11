from django.shortcuts import render

# Create your views here.
def marks(request):
    return render(request, 'marks.html')