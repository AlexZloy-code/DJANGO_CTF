from django import forms
from users.models import User
from web_tasks.models import Jobs, UserJobs


class LoginForm(forms.Form):
    name = forms.CharField(label="Название команды", max_length=255, required=True)
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput, required=True
    )


class UserAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password", "fine"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class MultipleJobsForm(forms.Form):
    jobs = forms.ModelMultipleChoiceField(
        queryset=Jobs.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    def save(self, user):
        jobs = self.cleaned_data["jobs"]
        for job in jobs:
            UserJobs.objects.create(user=user, job=job)
