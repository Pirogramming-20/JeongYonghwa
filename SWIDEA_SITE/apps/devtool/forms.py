from django import forms
from .models import *

class DevtoolRegisterForm(forms.ModelForm):
    class Meta:
        model = Devtool
        fields = '__all__'