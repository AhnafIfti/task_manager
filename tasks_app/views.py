from django.shortcuts import render, redirect
from .models import Category, Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    task_list = Task.objects.order_by('title')
    task_list_dictionary = {'tasks': task_list, 'title': 'List | Task'}
    return render(request, 'task_list.html', context=task_list_dictionary)

def task_detail(request, task_id):
    status_options = (
        (1, "Pending"),
        (2, "In Progress"),
        (3, "Completed"),
    )
    priority_options = (
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    )

    task_details = Task.objects.get(pk=task_id)
    
    for optionId, optionName in priority_options:
        if task_details.priority == optionId:
            task_details.priority = optionName

    for optionId, optionName in status_options:
        if task_details.status == optionId:
            task_details.status = optionName

    task_detail_dictionary = {'task_info':task_details, 'priority_options': priority_options, 'status_options': status_options, 'title': 'Detail | Task'}
    return render(request, 'task_detail.html', context=task_detail_dictionary)

def task_create(request):
    newTaskForm = TaskForm()

    if request.method == 'POST':
        newTaskForm = TaskForm(request.POST)

        if newTaskForm.is_valid():
            newTaskForm.save(commit=True)
            return redirect('tasks_app:task_list')
    else:
        newTaskForm = TaskForm()
        
    task_create_dictionary = {'title': 'Create | Task', 'taskForm': newTaskForm}
    return render(request, 'task_create.html', context=task_create_dictionary)

def category_list(request):
    category_list = Category.objects.order_by('name')
    category_list_dictionary = {'categories': category_list, 'title': 'List | Category'}
    return render(request, 'category_list.html', context=category_list_dictionary)

def category_tasks(request, category_id):
    category_info = Category.objects.get(pk = category_id)
    task_info = Task.objects.filter(category=category_info)
    category_task_dictionary = {'category_info':category_info, 'category_task_info': task_info, 'title': 'Task | Category'}
    return render(request, 'category_tasks.html', context=category_task_dictionary)