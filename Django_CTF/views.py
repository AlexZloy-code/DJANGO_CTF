from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, 'Django_CTF/404.html')