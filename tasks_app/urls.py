from django.urls import path
from tasks_app import views

app_name = "tasks_app"

urlpatterns = [
    path('task-list/', views.task_list, name="task_list"),
    path('category-list/', views.category_list, name="category_list"),
]