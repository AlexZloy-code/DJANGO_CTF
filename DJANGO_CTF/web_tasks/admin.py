from django.contrib import admin
from web_tasks.models import Jobs, UserJobs
from main.forms import JobsForm
from django.contrib import admin
from .models import Jobs


def mark_jobs_as_completed(modeladmin, request, queryset):
    for i in queryset:
        i.show = 0 if i.show else 1
        i.save()


mark_jobs_as_completed.short_description = "Поменять показ работ"


class JobsAdmin(admin.ModelAdmin):
    form = JobsForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "type",
                    "full_name",
                    "balls",
                    "creator",
                    "job",
                    "img",
                    "link",
                    "flag",
                    "show",
                )
            },
        ),
    )

    list_display = ("full_name", "creator", "balls", "type", "show")

    search_fields = ("full_name", "creator")

    list_filter = ("type", "show")

    actions = [mark_jobs_as_completed]


admin.site.register(Jobs, JobsAdmin)
