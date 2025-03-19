from django.shortcuts import render

# Create your views here.
def task_list(request):
    task_list_dictionary = {'title': 'List | Task'}
    return render(request, 'task_list.html', context=task_list_dictionary)

def category_list(request):
    category_list_dictionary = {'title': 'List | Category'}
    return render(request, 'category_list.html', context=category_list_dictionary)