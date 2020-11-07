from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_protect

from myApp import models


def login(request):
    return render(request,"login.html");

def logintest(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    # user = models.teacher.get(name=username)
    # passw = models.teacher.get(name=password)
    if username == "0001" and password == "0001":
        return HttpResponseRedirect("/vote/")
    else:
        return HttpResponse("login fail")

def test(request):
    return render(request,'test.html')

def vote(request):
    return render(request,'Vote.html')
