from django.contrib import admin
from django.urls import path, include
from tasks_app import views

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks_app.urls')),
]
