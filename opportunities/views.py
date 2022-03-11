from .models import opportunities
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect


@method_decorator(cache_page(60*60*12),name='dispatch')
class jobslist(generic.ListView):
    queryset = opportunities.objects.all().order_by('-time')
    template_name = 'opportunities.html'
    paginate_by = 5

def resume(request):
    return render(request, "resume.html", context=None)