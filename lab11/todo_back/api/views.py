from django.shortcuts import render
from .models import TaskList, Task
from django.http import JsonResponse
from django.http import HttpResponse


def list(request):
    tasks = TaskList.objects.all()
    json_tasks = [task.to_json_list() for task in tasks]
    return JsonResponse(json_tasks, safe=False)


def list_id(request, pk):
    try:
        tasks_id = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExit as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(tasks_id.to_json_list(), safe=False)


def task(request, pk):
    try:
        t_task = TaskList.objects.get(id=pk)
    except Task.DoesNotExit as e:
        return JsonResponse({'error': str(e)}, safe=False)
    json_t_task = [t.to_json_detail() for t in t_task.tasks.all()]
    return JsonResponse(json_t_task, safe=False)



def task_detail(request, pk):
    try:
        detail = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(detail.to_json_detail())