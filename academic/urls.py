from django.urls import path, include

from . import views

urlpatterns = [
    path('timetables', views.schedule, name="timetable"),
    path('syllabus-credits', views.syllabuscredits, name="credits"),
    path('notes',views.notes,name="notes")
]