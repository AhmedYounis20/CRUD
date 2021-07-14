from django import forms
from .models import * 




class makeForm(forms.ModelForm):
    class Meta:
        model=make
        fields=['name']

class autoForm(forms.ModelForm):
    class Meta:
        model=auto
        fields=['Nickname','Mileage','Comments','make']
    