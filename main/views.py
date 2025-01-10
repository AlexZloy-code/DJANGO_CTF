from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import User
from main.utils import check_flag
from web_tasks.models import Jobs


def main_website(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))
    return render(request, "main/CTF.html", {"title": "CTF"})


@login_required(login_url='/users/login/')
def rating(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    users_with_balls = []
    
    for user in list(User.objects.filter(show=True)):
        balls = user.fine + sum(job.balls for job in user.jobs.all() if job.show)
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        if sorted_table[i][1]:
            prochent = sorted_table[i][1] // (sum([i.balls for i in Jobs.objects.filter(show=True) if i.balls > 0]) // 100)
            sorted_table[i] = (i,) + sorted_table[i] + (int(prochent * 9.5),)
        else:
            sorted_table[i] = (i,) + sorted_table[i] + (0,)
    return render(request, "main/rating.html", {"table": sorted_table, 'angle': 180 / (len(sorted_table) - 1) if len(sorted_table) > 1 else 90})


@login_required(login_url='/users/login/')
def rating_pro(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    users_with_balls = []
    
    for user in list(User.objects.all()):
        balls = user.fine + sum(job.balls for job in user.jobs.all() if job.show)
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        if sorted_table[i][1]:
            prochent = sorted_table[i][1] // (sum([i.balls for i in Jobs.objects.filter(show=True) if i.balls > 0]) // 100)
            sorted_table[i] = (i,) + sorted_table[i] + (int(prochent * 9.5),)
        else:
            sorted_table[i] = (i,) + sorted_table[i] + (0,)
    return render(request, "main/rating_pro.html", {"table": sorted_table, 'angle': 180 / (len(sorted_table) - 1) if len(sorted_table) > 1 else 180})


@login_required(login_url='/users/login/')
def rating1(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    users_with_balls = []

    for user in list(User.objects.all()):
        balls = user.fine + sum(job.balls for job in user.jobs.all() if job.show)
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        sorted_table[i] = (i + 1,) + sorted_table[i]
    return render(request, "main/rating1.html", {"table": sorted_table})


@login_required(login_url='/users/login/')
def ball_changer(request, command, balls):
    if request.user.is_superuser:
        try:
            target_user = User.objects.get(username=command)
            target_user.fine -= int(balls)
            target_user.save()
        except User.DoesNotExist:
            return HttpResponseNotFound("User not found")
    return render(request, "main/CTF.html", {"title": "CTF"})