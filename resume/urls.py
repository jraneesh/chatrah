from django.urls import path

from . import views

urlpatterns = [
    path("resume-form", views.home, name="resume-form"),
    path("resume-download", views.download, name="resume-download")
]