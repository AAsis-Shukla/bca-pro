from django.shortcuts import render

# Create your views here.

def zolo(request):
    return render(request,"index.html")