from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import User
from main.utils import check_flag


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
        balls = user.fine + sum(job.balls for job in user.jobs.all())
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        sorted_table[i].insert(0, i)
    return render(request, "main/rating.html", {"table": sorted_table})


@login_required(login_url='/users/login/')
def rating1(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    users_with_balls = []

    for user in list(User.objects.filter(show=True)):
        balls = user.fine + sum(job.balls for job in user.jobs.all())
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        sorted_table[i].insert(0, i)
    
    return render(request, "main/rating1.html", {"table": sorted_table})


@login_required(login_url='/users/login/')
def rating2(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    users_with_balls = []

    for user in list(User.objects.filter(show=True)):
        balls = user.fine + sum(job.balls for job in user.jobs.all())
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        sorted_table[i].insert(0, i)
    
    return render(request, "main/rating2.html", {"table": sorted_table})


@login_required(login_url='/users/login/')
def rating5(request):
    if request.method == "POST":
        check_flag(request.user, request.POST.get("input_flag"))

    users_with_balls = []

    for user in list(User.objects.filter(show=True)):
        balls = user.fine + sum(job.balls for job in user.jobs.all())
        users_with_balls.append((user.username, balls))

    sorted_table = sorted(users_with_balls, key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_table)):
        sorted_table[i].insert(0, i)
        
    return render(request, "main/rating5.html", {"table": sorted_table})


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


def get_my_ip(request):
    ip = request.headers.get("X-Forwarded-For", request.META["REMOTE_ADDR"])
    return JsonResponse({"ip": ip})


def download_file(request, filename):
    file_path = f"tasks/{filename}"
    response = HttpResponse(open(file_path), content_type="application/octet-stream")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
