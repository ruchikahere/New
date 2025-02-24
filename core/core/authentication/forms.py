from django import forms
from .models import Profile
from .models import Document


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'picture']  

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
