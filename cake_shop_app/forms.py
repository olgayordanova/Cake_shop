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
        # CharField(max_length=10, choices=TYPE_CHOICES,)

# from django import forms
#
# class ContactForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)
#
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass