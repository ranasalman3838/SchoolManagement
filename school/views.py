from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'frontend.html')

def backend(request):
    return render(request,'backend.html')

# def frontend(request):
#     return render(request,'frontend.html')