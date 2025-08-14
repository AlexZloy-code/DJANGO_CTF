import os
from django.http import FileResponse, Http404
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from web_tasks.models import Jobs
from main.utils import check_flag
from users.models import User


@login_required(login_url="/users/login/")
def tasks(request):
    if request.method == "POST":
        messange = check_flag(request.user,
                              request.POST.get("input_flag"),
                              request.user.is_superuser)
    else:
        messange = None


    users_with_balls = []

    jobs = Jobs.objects.filter(show=True)

    for i in range(len(jobs)):
        jobs[i].flag = "Not cheating"

    for user in list(User.objects.all()):
        balls = user.fine + sum(job.balls for job in user.jobs.all() if job.show)
        users_with_balls.append((user.username, balls))

    return render(
        request,

        "web_tasks/tasks.html",

        {
            "title": "Журнал работ",
            "jobs": jobs,
            "users_table": users_with_balls,
            "messange": messange,
        },
    )


@login_required(login_url="/users/login/")
def task(request, pk):
    if request.method == "POST":
        messange = check_flag(request.user,
                              request.POST.get("input_flag"),
                              request.user.is_superuser)
    else:
        messange = None


    job = get_object_or_404(Jobs, pk=pk, show=True)
    job.flag = "Not cheating"

    if job:
        return render(
            request,

            "web_tasks/task.html",

            {
                "title": "Журнал работ",
                "job": job,
                "messange": messange,
            },
        )


@login_required(login_url="/users/login/")
def web_task(request, link):
    if request.method == "POST":
        messange = check_flag(request.user,
                              request.POST.get("input_flag"),
                              request.user.is_superuser)
    else:
        messange = None


    """ 
    Пока что не используется
    
    if link not in ["web3/robots.txt", "help_for_ctf_task_crypto"]:
        get_object_or_404(Jobs, link=link, show=True) """

    if "." not in link or "/" in link:
        return render(request,
                      
                      "tasks/" + link + ".html",
                      
                      {
                        "messange": messange,
                      },
                    )
    else:
        file_path = os.path.join(settings.BASE_DIR, "tasks", link)

        if os.path.exists(file_path):
            response = FileResponse(open(file_path, "rb"), as_attachment=True)
            response["Content-Disposition"] = f'attachment; filename="{link}"'
            return response
        else:
            raise Http404("Файл не найден")
