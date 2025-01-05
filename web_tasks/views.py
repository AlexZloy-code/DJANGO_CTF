from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from web_tasks.models import Jobs
from main.utils import check_flag


@login_required(login_url='/users/login/')
def tasks(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    jobs = Jobs.objects.filter(show=True)

    return render(request, "web_tasks/tasks.html", {"title": "Журнал работ", "jobs": jobs})


@login_required(login_url='/users/login/')
def task(request, pk):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    job = Jobs.objects.filter(pk=pk).first()

    if job:
        return render(request, "web_tasks/task.html", {"title": "Журнал работ", "job": job})
    
    return render(request, "web_tasks/no_task.html")
