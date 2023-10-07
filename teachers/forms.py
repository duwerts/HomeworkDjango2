from django import forms
from .models import Teacher, Group


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "last_name", "subject", "birth_data"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "curator"]
