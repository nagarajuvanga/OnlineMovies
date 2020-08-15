from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from app.forms import Usersignup,Userlogin
from app.models import Movietable, Userlogintable, Usersignuptable
from task.settings import MOVIES_FILE
import json

def showIndex(request):
    return render(request,"home.html",{"data":Movietable.objects.all()})


def savemovie(request):
    name = request.GET.get("m_name")
    type = request.GET.get("m_type")
    rank = request.GET.get("m_rank")
    cast = request.GET.get("m_cast")
    year = request.GET.get("m_release")
    image = request.GET.get("m_image")
    Movietable(moviename=name, t_ype=type, rank=rank, casting=cast, release=year,image=image).save()
    return render(request,'index.html',{"data":movies})


def login(request):
    return render(request,"login.html")


def save_login(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    if un == "nagaraju" and pa == "nagaraju":
        dict_data = json.loads(open(MOVIES_FILE).read())
        global movies
        movies = [x for x in dict_data['d']]
        return render(request, "index.html", {"data": movies})
    else:
        messages.error(request, "Invalid User")
        return render(request,"login.html")

def signuppage(request):
    return render(request, "usersignup.html", {"forms":Usersignup})

def savesignup(request):
    x=request.POST.get("username")
    y=request.POST.get("pas")
    us=Usersignup(request.POST)
    if us.is_valid():
        us.save()
        Userlogintable(usrname=x, pas=y).save()
        messages.success(request,"SignUp Successfully")
        return redirect("signuppage")
    else:
        messages.error(request,"Invalid Details")
        return redirect("signuppage")

def userlogin(request):
    return render(request, "userlogin.html", {"forms":Userlogin})

def userloginhome(request):
    n = request.POST.get("usrname")
    a = request.POST.get("pas")
    na = request.GET.get("usrname")
    p = request.GET.get("pas")
    try:
        usr = Userlogintable.objects.get(usrname=n or na, pas=a or p)
        result = Movietable.objects.all()
        pg = Paginator(result,3)
        next = request.GET.get("next")
        if next:
                res = pg.page(next)
                return render(request, "userpage.html", {"data":res,"user":usr})
        else:
            res = pg.page(1)
            return render(request, "userpage.html", {"data": res,"user":usr})
    except Userlogintable.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect("userlogin")


def searchaction(request):
    x=request.POST.get("s1")
    try:
        a = Movietable.objects.filter(moviename__contains=x)
        return render(request, "searchpage.html",{"data":a})
    except Movietable.DoesNotExist:
        messages.error(request,"Not Found")
        return render(request, "searchpage.html")