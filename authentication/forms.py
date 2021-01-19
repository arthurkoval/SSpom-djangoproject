from django import forms
from .models import CustomUser

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class UserForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'form-control','style':'width: 200px;'}))
    # middle_name = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class' : 'form-control','style':'width: 200px;'}))
    # last_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'form-control','style':'width: 200px;'}))
    # email = forms.EmailField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'form-control','style':'width: 200px;'}))
    # password = forms.CharField(max_length=128,required=True,widget=forms.TextInput(attrs={'class' : 'form-control','style':'width: 200px;'}))
    # role = forms.ChoiceField(choices = ROLE_CHOICES, required=True)
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name','last_name','email','password','role']