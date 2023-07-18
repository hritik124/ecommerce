from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class Registration(UserCreationForm):
    class Meta:
        password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'abc'}))
        password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'abc'}))
        model = User
        fields={'username','first_name','last_name','email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'abc'}),
            'first_name':forms.TextInput(attrs={'class':'abc'}),
            'last_name':forms.TextInput(attrs={'class':'abc'}),
            'email':forms.TextInput(attrs={'class':'abc'})
        }

class Loginform(AuthenticationForm):
    pass  