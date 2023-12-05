"""Forms of the project."""
from django.forms import ModelForm
from things.models import Thing
from django import forms


# Create your forms here.
class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    description = forms.Textarea()
    quantity = forms.NumberInput()
