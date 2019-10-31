from django import forms
from django.forms import PasswordInput

from authapp.models import Register


class RegForm(forms.ModelForm):
    class Meta:
        model=Register
        widgets = {'pwd': forms.PasswordInput(),'cpwd':forms.PasswordInput()}
        fields = ['fname', 'phno', 'email', 'uname', 'pwd', 'cpwd']

class LoginForm(forms.ModelForm):
    uname=forms.CharField(max_length=20)
    pwd=forms.CharField(widget=forms.PasswordInput())