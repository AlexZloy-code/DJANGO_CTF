from django.urls import path
from web_tasks.models import Jobs
from web_tasks.views import (
    tasks,
    task,
)

app_name = "tasks"

urlpatterns = [
    path("", tasks, name="tasks"),
    path("<int:pk>/", task, name="tasks"),
]
