from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age']
        name = forms.CharField(
        label="Student Name",  # Label displayed in the form
        max_length=100,
        error_messages={
            'required': "Please enter your name!",
            'max_length': "Name cannot exceed 100 characters."
        }
    )
    
    email = forms.EmailField(
        label="Email Address",  # Label displayed in the form
        error_messages={
            'required': "Email is required!",
            'invalid': "Enter a valid email address!"
        }
    )
        
