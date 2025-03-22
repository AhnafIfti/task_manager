from django.contrib import admin
from django.urls import path, include
from tasks_app import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks_app.urls')),
]

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
