from django import forms
from django.contrib.auth.models import User
from .models import Profile, Task

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_date', 'task_description']
