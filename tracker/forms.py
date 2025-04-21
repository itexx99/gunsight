from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'date_out', 'status', 'notes']
        widgets = {
            'date_out': forms.DateInput(attrs={'type': 'date'}),
        }
