from django.urls import path, re_path
from web_tasks.views import (
    tasks,
    task,
    web_task,
)

app_name = "tasks"

urlpatterns = [
    path("", tasks, name="tasks"),
    path("<int:pk>/", task, name="task_detail"),
    re_path(r'^(?P<link>.+)/$', web_task, name='other')
]
