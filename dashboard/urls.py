from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.notifications, name="dashboard"),
    #path("class", views.classupdates, name="classupdates")
]