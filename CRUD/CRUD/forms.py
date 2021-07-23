from django import forms



class loginForm(forms.Form):
    username=forms.CharField(label="Username:")
    password=forms.CharField(label='password',widget=forms.PasswordInput)
