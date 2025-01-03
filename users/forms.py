from django import forms
from users.models import User


class LoginForm(forms.Form):
    name = forms.CharField(label="Название команды", max_length=255, required=True)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=True)


class UserAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'fine']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
