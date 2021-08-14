from .models import Product
from django import forms


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'type': forms.TextInput ( attrs={'class': 'form-control'} ),
        }
        fields = '__all__'
