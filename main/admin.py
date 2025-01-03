from django.contrib import admin
from main.models import Jobs, UserJobs
from main.forms import JobsForm

class JobsAdmin(admin.ModelAdmin):
    form = JobsForm
    
    list_display = ('full_name', 'creator', 'balls', 'type')

    search_fields = ('full_name', 'creator')

    list_filter = ('type',)


admin.site.register(Jobs, JobsAdmin)


@admin.register(UserJobs)
class UserJobsAdmin(admin.ModelAdmin):
    list_display = ("user", "job", "date_assigned")
    search_fields = ("user__username", "job__full_name")
    list_filter = ("date_assigned",)


class CustomAdminSite(admin.AdminSite):
    site_header = 'My Admin'
    site_title = 'My Admin Portal'
    index_title = 'Welcome to My Admin Portal'

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = True
        return context


admin_site = CustomAdminSite(name='custom_admin')