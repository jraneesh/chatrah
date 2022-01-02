from django.shortcuts import render
from .models import timetable, syllabus_credit,notebook
from users.models import student
from django.contrib.auth import get_user
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def schedule(request):
    userid = get_user(request)
    s_class = student.objects.get(number=userid)
    tt_img = timetable.objects.filter(year=s_class.year).filter(dept=s_class.dept).filter(section=s_class.section)
    tt = dict()
    for item in tt_img:
        tt[item.title] = item.timetable
    return render(request, "timetable.html", {'tt': tt})

@login_required
def syllabuscredits(request):
    userid = get_user(request)
    s_class = student.objects.get(number=userid)
    s_c = syllabus_credit.objects.filter(dept=s_class.dept)
    depts = dict(student.depts)
    sc = list()
    for val in s_c:
        sc.append({"reg":val.reg,"dept":depts[val.dept],"link":val.link})
    return render(request, "sc.html", {'sc': sc})

@login_required
def notes(request):
    userid = get_user(request)
    s_class = student.objects.get(number=userid)
    noteslink = notebook.objects.filter(year=s_class.year).filter(dept=s_class.dept).filter(section=s_class.section)
    paginator = Paginator(noteslink,1)
    page = request.GET.get('page')
    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        links = paginator.page(1)
    except EmptyPage:
        links = paginator.page(paginator.num_pages)
    return render(request, "notes.html",{"links":links})
