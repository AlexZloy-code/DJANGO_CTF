from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from users.forms import UserAdminForm


class CustomUserAdmin(UserAdmin):
    form = UserAdminForm

    fieldsets = (
        (None, {"fields": ('username', 'password', 'fine')}),
    )

    list_display = ('username', 'password', 'fine')
    search_fields = ('username', 'fine')


admin.site.register(User, CustomUserAdmin)