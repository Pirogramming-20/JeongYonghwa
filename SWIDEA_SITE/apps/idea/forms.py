from django import forms
from .models import Idea

class IdeaRegisterForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'
        exclude = ['marked']