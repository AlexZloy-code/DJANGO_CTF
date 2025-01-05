from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.admin import UserAdmin
from users.models import User
from users.forms import UserAdminForm
from web_tasks.models import Jobs, UserJobs
from users.forms import MultipleJobsForm


class UserJobsInline(admin.TabularInline):
    model = UserJobs
    extra = 1


def mark_users_as_completed(modeladmin, request, queryset):
    for i in queryset:
        i.show = 0 if i.show else 1
        i.save()


mark_users_as_completed.short_description = "Поменять показ команд"


class CustomUserAdmin(UserAdmin):
    inlines = [UserJobsInline]
    form = UserAdminForm

    fieldsets = (
        (None, {"fields": ('username', 'password', 'fine', 'show')}),
    )

    list_display = ('username', 'password', 'fine', 'show')
    search_fields = ('username', 'fine', 'show')

    actions = [mark_users_as_completed]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/add_jobs/', self.admin_site.admin_view(self.add_jobs), name='add_jobs'),
        ]
        return custom_urls + urls

    def add_jobs(self, request, object_id):
        user = self.get_object(request, object_id)
        if request.method == 'POST':
            form = MultipleJobsForm(request.POST)
            if form.is_valid():
                form.save(user)
                self.message_user(request, "Работы успешно добавлены.")
                return redirect('..')
        else:
            form = MultipleJobsForm()
        
        context = {
            'form': form,
            'user': user,
            'opts': self.model._meta,
            'title': f'Добавить работы для {user.username}',
        }
        return render(request, 'admin/add_jobs.html', context)


admin.site.register(User, CustomUserAdmin)