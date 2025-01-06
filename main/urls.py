from django.urls import path
from main.views import (
    main_website,
    rating,
    ball_changer,
)

app_name = "main"

urlpatterns = [
    path("", main_website, name="main_website"),
    path("rating/", rating, name="rating"),
    path("rating1/", rating, name="rating"),
    path("rating2/", rating, name="rating"),
    path("rating5/", rating, name="rating"),
    path("ball_changer/<str:command>/<int:balls>/", ball_changer, name="ball_changer"),
]
