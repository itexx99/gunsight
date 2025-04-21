from django import forms
from django.forms import inlineformset_factory
from .models import Order, GunPart

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer',
            'status',
            'notes',
            'wants_engraving',
            'wants_electroplating',
        ]
        widgets = {
            'date_out': forms.DateInput(attrs={'type': 'date'}),
        }

class GunPartForm(forms.ModelForm):
    class Meta:
        model = GunPart
        fields = [
            'name',
            'serial_number',
            'part_type',
            'finish',
            'design',
            'image',
        ]

GunPartFormSet = inlineformset_factory(
    Order,
    GunPart,
    form=GunPartForm,
    extra=1,
    can_delete=True
)