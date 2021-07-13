from django import forms
from .models import * 




class makeForm(forms.ModelForm):
    class Meta:
        model=make
        fields=['name']
    