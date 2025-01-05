import os
from django.http import FileResponse, Http404
from django.conf import settings
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

    job = Jobs.objects.filter(pk=pk, show=True).first()

    if job:
        return render(request, "web_tasks/task.html", {"title": "Журнал работ", "job": job})
    
    return render(request, "web_tasks/no_task.html")


@login_required(login_url='/users/login/')
def web_task(request, link):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    job = Jobs.objects.filter(link=link, show=True).first()

    if job:
        if '.' not in link:
            return render(request, 'tasks/' + link + '.html')
        else:
            file_path = os.path.join(settings.BASE_DIR, 'tasks', link)

            if os.path.exists(file_path):
                response = FileResponse(open(file_path, 'rb'), as_attachment=True)
                response['Content-Disposition'] = f'attachment; filename="{link}"'
                return response
            else:
                raise Http404("Файл не найден")
    
    return render(request, "web_tasks/no_task.html")
