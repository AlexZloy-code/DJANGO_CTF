from django.db import models
from users.models import User


class Jobs(models.Model):
    type = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    balls = models.IntegerField(null=True)
    creator = models.CharField(max_length=255, null=True)
    job = models.TextField(null=True)
    img = models.ImageField(upload_to='job_images/', null=True)
    link = models.URLField(null=True, blank=True)
    flag = models.CharField(max_length=255, null=True)
    show = models.BooleanField("Показывать?")

    users = models.ManyToManyField(User, through="UserJobs", related_name="jobs")

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.full_name or "Unnamed Job"


class UserJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    date_assigned = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Работа - команда"
        verbose_name_plural = "Работы - команды"
