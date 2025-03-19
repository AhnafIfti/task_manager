from django.shortcuts import render
from tasks_app.models import Category

# Create your views here.
def task_list(request):
    task_list_dictionary = {'title': 'List | Task'}
    return render(request, 'task_list.html', context=task_list_dictionary)

def category_list(request):
    category_list = Category.objects.order_by('name')
    category_list_dictionary = {'categories': category_list, 'title': 'List | Category'}
    return render(request, 'category_list.html', context=category_list_dictionary)