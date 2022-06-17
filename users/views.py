from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import student
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests,json,ast


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

@login_required
def applyleave(request):
    if request.method == "GET":
        return render(request, "absentmsg.html", context=None)
    userid = get_user(request)
    Student = student.objects.get(number=userid)
    leave_msg = request.POST["msg"]
    sections = {1:"A",2:"B",3:"C"}
    depts = {1:"CSE",2:"CIVIL",3:"EEE",4:"IT",5:"ECE",6:"MECH",7:"EIE"}
    msg = {"sid":Student.number,"year":Student.year,"dept":depts[Student.dept],"section":sections[Student.section],"msg":leave_msg}
    res = requests.post("http://127.0.0.1:8000/setmsg", data=json.dumps(msg), headers={"Content-Type":"application/json","Authorization":"Bearer 04ba96760fa247b8b39e79bb1cfece71"})
    if res.status_code==204:
        return render(request, "msgreply.html", context={"msg": "Message sent Successfully"})
    else:
        return render(request, "msgreply.html", context={"msg": "Message sent Successfully"})

@login_required
def checkattendance(request):
    userid = get_user(request)
    Student = student.objects.get(number=userid)
    sections = {1:"A",2:"B",3:"C"}
    depts = {1:"CSE",2:"CIVIL",3:"EEE",4:"IT",5:"ECE",6:"MECH",7:"EIE"}
    data = {"id":Student.number,"year":Student.year,"dept":depts[Student.dept],"section":sections[Student.section]}
    res = requests.post("http://127.0.0.1:8000/checkattendance", data=json.dumps(data), headers={"Content-Type":"application/json","Authorization":"Bearer 04ba96760fa247b8b39e79bb1cfece71"})
    if res.status_code==200:
        attd = ast.literal_eval(json.loads(res.content))
        low_attd = True if attd['total_percent']<65 else False
        del attd['id']
        del attd['class']
        return render(request, "checkattd.html", {'attd':attd, 'low_attd':low_attd})
    else:
        print("error")

def offline(request):
    return render(request, "offline.html", context=None)

def sw(request):
    return render(request, 'serviceworker.js',context=None,content_type="application/javascript")
