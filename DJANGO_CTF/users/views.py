from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from users.forms import LoginForm
from django.urls import reverse
from django.contrib.auth.models import User


@login_required(login_url='/users/login/')
def add_user(request, command):
    if request.user.is_superuser:  # Проверка на администраторов
        User.objects.get_or_create(username=command)
    return render(request, "CTF.html", {"title": "CTF"})


@login_required(login_url='/users/login/')
def delete_user(request, command):
    if request.user.is_superuser:  # Проверка на администраторов
        try:
            user_to_delete = User.objects.get(username=command)
            user_to_delete.delete()
        except User.DoesNotExist:
            return HttpResponseNotFound("User not found")
    return render(request, "CTF.html", {"title": "CTF"})


@login_required(login_url='/users/login/')
def logout_view(request):
    auth_logout(request)
    return redirect(reverse("main:main_website"))


def login_view(request):
    form = LoginForm()  # Создаем пустую форму

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("tasks:tasks")
            else:
                return render(
                    request,
                    "users/login.html",
                    {
                        "form": form,
                        "message": "Неправильное имя пользователя или пароль.",
                    },
                )

    return render(request, "users/login.html", {"form": form})