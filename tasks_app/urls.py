from django.urls import path
from . import views

app_name = "tasks_app"

urlpatterns = [
    path('task-list/', views.task_list, name="task_list"),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('task-create/', views.task_create, name='task_create'),
    path('category-list/', views.category_list, name="category_list"),
    path('category/<int:category_id>/', views.category_tasks, name='category_tasks'),
]