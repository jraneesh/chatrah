from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import student
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect("/login")
    
def signup(request):
    if request.method == "GET":
        return render(request, "register.html", context=None)
    _name = request.POST["name"]
    _number = request.POST["number"]
    _yoa = request.POST["yoa"]
    _year = request.POST["year"]
    _dept = request.POST["dept"]
    _section = request.POST["section"]
    _password = request.POST["pwd"]
    join = student(name=_name, number=_number, YoA=_yoa, year=_year, dept=_dept, section=_section)
    join.save()
    User.objects.create_user(_number,"NULL", _password)
    return redirect("/login")


def loginstudent(request):
    if request.method == "GET" and request.session._session_key is None:
        return render(request, "login.html", context=None)
    elif request.session._session_key is not None:
        key = request.session._session_key
        if request.session.get(key) is None:
            return redirect("/login")
        else:
            return redirect("/profile")
    else:
        _number = request.POST["number"]
        _password = request.POST["pwd"]
        user = authenticate(request, username=_number, password=_password)
        if user is not None:
            login(request, user)
            return redirect("/profile")
        else:
            return HttpResponse("Username/Password Incorrect")

@login_required
def profile(request):
    userid = get_user(request)
    if userid is None:
        return redirect("/login")
    user = student.objects.get(number=userid)
    years = dict(student.years)
    sections = dict(student.sections)
    depts = dict(student.depts)
    return render(request, "profile.html", context={"name": user.name, "number": user.number, "YoA": user.YoA, "year": years[user.year], "dept": depts[user.dept],"section": sections[user.section]})
    
@login_required
def logoutstudent(request):
    logout(request)
    return redirect("/login")

