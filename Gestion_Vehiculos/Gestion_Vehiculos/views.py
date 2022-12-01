from django.http import HttpResponse
import requests
from django.shortcuts import render

url = "http://localhost"

def login(request):
    #GET
    return render(request, "login.html")
