from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import notification
from users.models import student
from django.contrib.auth import get_user
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def notifications(request):
    userid = get_user(request)
    s_class = student.objects.get(number=userid)
    notification_updates = notification.objects.filter(Q(year=5) | Q(year=s_class.year)).filter(Q(dept=8) | Q(dept=s_class.dept)).filter(Q(section=4) | Q(section=s_class.section)).order_by('-time').values("title","content","time")
    paginator = Paginator(notification_updates,2)
    page = request.GET.get('page')
    try:
        updates = paginator.page(page)
    except PageNotAnInteger:
        updates = paginator.page(1)
    except EmptyPage:
        updates = paginator.page(paginator.num_pages)
    return render(request, "dashboard.html", {'dash': updates})