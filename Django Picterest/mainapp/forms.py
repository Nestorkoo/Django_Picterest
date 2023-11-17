from django import forms
from .models import Categories, Create_Post
from django.forms import *


class AddCardImage(ModelForm):
    class Meta:
        model = Create_Post
        fields = [
            'name',
            'photo',
            'category',
            'description',
        ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'name_of_post',
                'placeholder': 'Дайте назву проекту'

            }),
            'photo': FileInput(),
            'description': Textarea(attrs={
            'class': 'description_of_post',
            'placeholder': 'Опишіть свої зображення!'
            })
        }


