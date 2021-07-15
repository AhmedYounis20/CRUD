from django import forms
from .models import * 




class breedForm(forms.ModelForm):
    class Meta:
        model=breed
        fields=['name']

class catForm(forms.ModelForm):
    class Meta:
        model=cat
        fields=['nickname','weight','foods','breed']
    