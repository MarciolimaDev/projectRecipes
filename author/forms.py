from cProfile import label
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def addAttr(field, attrName, attrNewValue):
    existing = field.field.widget.attrs.get(attrName, '')
    field.field.widget.attrs[attrName] = f'{existing} {attrNewValue}'.strip()


def addPlaceholder(field, placeholderVal):
    addAttr(field, 'placeholder', placeholderVal)


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addPlaceholder(self['first_name'], 'Ex. João')
        addPlaceholder(self['last_name'], 'Ex. Silva')
        addPlaceholder(self['username'], 'Ex. joaosilva')
        addPlaceholder(self['email'], 'Ex. Digite seu Email')

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


    #validar campos senha e confirmar senha
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password':'As Senhas não conferem',
                'password2': 'As Senhas não conferem',}, code='invalid',)

        


    
