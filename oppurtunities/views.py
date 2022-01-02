from django.shortcuts import render
from .models import oppurtunities
from django.views import generic

class jobslist(generic.ListView):
    queryset = oppurtunities.objects.all().order_by('-time')
    template_name = 'oppurtunities.html'
    paginate_by = 5