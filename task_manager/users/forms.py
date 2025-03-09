from django import forms
from django.forms import ModelForm

from .models import CustomUser


class CustomUserForm(ModelForm):
    '''Form for CustomUser model.'''
    class Meta:
        model = CustomUser

        # what fields here? 
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            # 'password',
        ]
