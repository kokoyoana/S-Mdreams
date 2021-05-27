from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class AgregarProductoForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    actualizar = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
