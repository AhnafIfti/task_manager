from django.contrib import admin
from tasks_app.models import Task, Category

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
