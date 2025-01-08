from django.urls import path
from main.views import (
    main_website,
    rating,
    rating1,
    ball_changer,
)

app_name = "main"

urlpatterns = [
    path("", main_website, name="main_website"),
    path("rating/", rating, name="rating"),
    path("rating1/", rating1, name="rating1"),
    path("ball_changer/<str:command>/<int:balls>/", ball_changer, name="ball_changer"),
]
