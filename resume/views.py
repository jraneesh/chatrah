from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "form.html", context=None)

@login_required
def download(request):
    if request.method == "GET":
        return redirect("/resume-form")
    data = dict(request.POST)
    out=dict()
    for k,v in data.items():
        out[k]=v[0]
    return render(request, "pdf.html", context=out)

