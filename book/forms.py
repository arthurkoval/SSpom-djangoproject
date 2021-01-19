from django import forms
from .models import Book
from author.models import Author



class CustomAuthorNameField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, author):
        return f'{author.name} {author.surname} {author.patronymic}'

class BookForm(forms.ModelForm):
    authors = CustomAuthorNameField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Book
        fields = ['name','description','count']