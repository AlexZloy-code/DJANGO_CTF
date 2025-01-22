from django.urls import path
from users.views import (
    login_view,
    add_user,
    delete_user,
    logout_view,
)

app_name = "users"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("add/<str:command>/", add_user, name="add_user"),
    path("delete/<str:command>/", delete_user, name="delete_user"),
    path("logout/", logout_view, name="logout"),
]
