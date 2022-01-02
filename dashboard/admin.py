from django.contrib import admin
from .models import notification
from django_summernote.admin import SummernoteModelAdmin


class updatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'time','year', 'dept', 'section')
    list_filter = ('year', 'dept', 'section','time')
    search_fields = [ 'year', 'dept', 'section']

admin.site.register(notification,updatesAdmin)
