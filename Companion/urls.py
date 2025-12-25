from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), 
    path('api/', include('base.api.urls')), 

    re_path(r'^favicon\.ico$', RedirectView.as_view( url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)