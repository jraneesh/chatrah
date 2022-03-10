from django.shortcuts import render
from .models import post
from django.views import generic
import mimetypes
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

def home(request):
    return render(request, "home.html", context=None)

@method_decorator(cache_page(60*60),name='dispatch')
class postlist(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'
    paginate_by = 3

@method_decorator(cache_page(60*60*12),name='dispatch')
class postdetail(generic.DetailView):
    model = post
    template_name = 'post_detail.html'