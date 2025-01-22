from django import forms
from web_tasks.models import Jobs


class TryForm(forms.Form):
    flag = forms.CharField(label="Название команды", max_length=100)


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ["type", "full_name", "balls", "creator", "job", "img", "link", "flag"]
