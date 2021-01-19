from django import forms
from .models import Author
from book.models import Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','surname','patronymic']