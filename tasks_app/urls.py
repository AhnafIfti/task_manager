from django.urls import path
from tasks_app import views

app_name = "tasks_app"

urlpatterns = [
    path('task-list/', views.task_list, name="task_list"),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('category-list/', views.category_list, name="category_list"),
]