from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, TextInput, EmailInput, TextInput, PasswordInput, FileInput
from .models import User



class signUpForm(UserCreationForm):

    password1 = forms.CharField(
            widget = forms.PasswordInput(attrs={
            'style': 'height:70%; width:100%; border:1px solid white; color:white; background:transparent; margin-top:15px; font-size:16px',
            })
    )

    password2 = forms.CharField(
            widget = forms.PasswordInput(attrs={
            'style': 'height:70%; width:100%; border:1px solid white; color:white; background:transparent; margin-top:15px; font-size:16px',
            })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets={
            'username':TextInput(attrs={
                'style': 'height:70%; width:100%; border:1px solid white; color:white; background:transparent; margin-top:15px;font-size:16px',
                }),
            'email':EmailInput(attrs={
                'style': 'height:70%; width:100%; border:1px solid white; color:white; background:transparent; margin-top:15px;font-size:16px',
                }),
            'profile_pic':FileInput(attrs={
                'style': 'height:70%; width:100%; border:1px solid white; color:white; background:transparent; margin-top:15px;font-size:16px',
                }),
		}