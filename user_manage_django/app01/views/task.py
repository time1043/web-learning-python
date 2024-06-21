from django.shortcuts import render


def task_list(request):
    """ 任务列表 """
    return render(request,'task/task_list.html')
