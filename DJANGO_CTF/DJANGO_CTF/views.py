from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, 'DJANGO_CTF/404.html')