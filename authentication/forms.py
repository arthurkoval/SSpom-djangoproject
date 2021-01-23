from django import forms
from .models import CustomUser

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name','last_name','email','password','role']