from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.admin import UserAdmin
from users.models import User
from users.forms import UserAdminForm
from web_tasks.models import UserJobs


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


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.register(User, CustomUserAdmin)