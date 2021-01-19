from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    end_at = forms.DateTimeField(widget=forms.SelectDateWidget())
    plated_end_at = forms.DateTimeField(widget=forms.SelectDateWidget())
    class Meta:
        model = Order
        fields = ['user','book','end_at','plated_end_at']