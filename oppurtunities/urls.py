from . import views
from django.urls import path

urlpatterns = [
    path('', views.jobslist.as_view(), name='grow'),
    path("resume", views.resume, name="resume-form"),
]