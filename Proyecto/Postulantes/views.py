from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<p>Bienvenido</p>")

def postulants(request):
    return render(request, 'index.html')
