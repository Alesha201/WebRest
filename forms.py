from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task,User, AbstractUser
from django.forms import ModelForm, TextInput, DateInput, Textarea, CheckboxInput, Select

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name","description", "completed", "due_date","priority","tasklist","Tag","User"]

        widgets = {
            "name": TextInput(attrs={
                'class': "form-control",
                'placeholder':'Название задачи',
                
            }),
            "description": TextInput(attrs={
                'class': "form-control",
                'placeholder':'Описание'
            }),
            "completed": CheckboxInput(attrs={
                
                'placeholder':'Выполнено'
            }),
            "due_date": DateInput(attrs={
                'class': "form-control",
                'placeholder':'Срок выполнения'
            }),
            "priority": Select(attrs={
                'class': "form-control",
                'placeholder':'Приоритет'
            }),
            "tasklist": Select(attrs={
                'class': "form-control",
            }),
            "Tag": Select(attrs={
                'class': "form-control",
                'placeholder':'Тег'
            }),
            "User": Select(attrs={
                'class': "form-control",
                
            }),
        }
