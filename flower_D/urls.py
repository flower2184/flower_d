from django.contrib import admin
from django.urls import path, include
from gameboard import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('gameboard/', include('gameboard.urls')),

    path('summernote/', include('django_summernote.urls')),

    path('common/', include('common.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

