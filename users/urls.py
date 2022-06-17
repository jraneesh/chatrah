from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.loginstudent, name="login"),
    path("profile", views.profile, name="profile"),
    path("logout", views.logoutstudent, name="logout"),
    path("applyleave",views.applyleave,name="applyleave"),
    path("offline",views.offline,name="offline"),
    path("serviceworker.js",views.sw,name="serviceworker.js"),
    path("checkattendance",views.checkattendance,name="checkattd")
]