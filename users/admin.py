from django.contrib import admin
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

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Если объект существует (т.е. редактируем существующего пользователя)
            form.base_fields['password'].initial = '********'  # Показываем звездочки вместо реального пароля
        return form

    def save_model(self, request, obj, form, change):
        # Если пользователь вводит новый пароль
        if form.cleaned_data['password'] and form.cleaned_data['password'] != '********':
            obj.set_password(form.cleaned_data['password'])
        obj.save()  # Сохраняем объект


admin.site.register(User, CustomUserAdmin)