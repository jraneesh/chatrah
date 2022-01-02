from . import views
from django.urls import path

urlpatterns = [
    path('', views.jobslist.as_view(), name='grow'),
]