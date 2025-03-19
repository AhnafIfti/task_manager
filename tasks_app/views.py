from django.shortcuts import render

# Create your views here.
def task_list(request):
    task_list_dictionary = {'title': 'List | Task'}
    return render(request, 'task_list.html', context=task_list_dictionary)