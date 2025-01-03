from django.urls import path
from main.views import (
    main_website,
    tasks,
    rating,
    ball_changer,
    get_my_ip,
)

app_name = "main"

urlpatterns = [
    path("", main_website, name="main_website"),
    path("tasks/", tasks, name="tasks"),
    path("rating/", rating, name="rating"),
    path("ball_changer/<str:command>/<int:balls>/", ball_changer, name="ball_changer"),
    path("get_my_ip/", get_my_ip, name="get_my_ip"),
]
