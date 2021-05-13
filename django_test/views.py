from django.shortcuts import render
from . import models

def home(request):
    return render(request,"home.html",{})

def register(request):
    if request.method=="GET":
        return render(request,"register.html",{"output":""})
    else:
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        gender=request.POST.get("gender")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        city=request.POST.get("city")
        '''
        print(name)
        print(username)
        print(password)
        print(gender)
        print(mobile)
        print(address)
        print(city)
        '''
        p=models.Register(name=name,username=username,password=password,gender=gender,mobile=mobile,address=address,city=city)
        p.save()
        return render(request,"register.html",{"output":"user registered successfully!"})

def showusers(request):
    userDeats=models.Register.objects.all()
    return render(request,"showusers.html",{"userDeats":userDeats})