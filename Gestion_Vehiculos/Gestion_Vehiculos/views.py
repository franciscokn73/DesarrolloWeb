from django.http import HttpResponse
import requests
from django.shortcuts import render

url = "http://localhost:8000"

def index(request):
    #GET
    print("entro a Mostrar")
    res = requests.get(url+"/select/vehiculo")
    if (res.status_code == 200):
        return render(request, "index.html", {"datos": res.json()})
    else:
        return HttpResponse("Error de comunicacion")

def login(request):
    #GET
    return render(request, "login.html")

def contruccion(request):
    #GET
    return render(request, "contruccion.html")
