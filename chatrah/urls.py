from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Chatrah'
admin.site.site_title = 'Chatrah'
admin.site.index_title = 'Chatrah Administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paper/', include('paper.urls')),
    path('', include('users.urls')),
    #path('', include('pwa.urls')),
    path('opportunities/', include('opportunities.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('academic/', include('academic.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

