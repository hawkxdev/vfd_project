from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from vfd_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('supplier.urls')),
    path('', include('vfd.urls')),
    path('', include('ips.urls')),
    path('', include('ss.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
