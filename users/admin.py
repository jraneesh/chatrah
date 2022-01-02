from django.contrib import admin
from .models import student

class students(admin.ModelAdmin):
    list_display=('name', 'number', 'year', 'dept', 'section')
    list_filter = ('year', 'dept', 'section')
    search_fields = ['number', 'year', 'dept', 'section']

admin.site.register(student, students)

