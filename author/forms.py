from cProfile import label
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
            'placeholder':'Confirme sua senha'
        }),
        label='Confirme sua senha')

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

        labels = {
            'first_name':'Nome',
            'last_name':'Sobrenome',
            'username':'Nome de usuário',
            'email':'Email',
            'password':'Senha'
        }

        help_texts = {
            'username':'Nome de usuário que será usado para fazer login',
            'email':'Email que será usado para fazer login'
        }

        widgets = {
            'password':forms.PasswordInput(attrs={
                'placeholder':'Digite sua senha'
            }),
        }

        


    
