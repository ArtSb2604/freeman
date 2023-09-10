from django import forms
from index.models import Advertisement


class CreateOrderForm(forms.ModelForm):
    img = forms.ImageField(required=False)
    currency = forms.ChoiceField(choices=[('Рубль (Россия)', 'Рубль (Россия)'), ('Доллар', 'Доллар'), ('Евро', 'Евро')])

    class Meta:
        model = Advertisement
        fields = ['title', 'categories', 'description', 'img', 'price', 'currency', 'address', 'contact_person', 'number_phone']
        widgets = {
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            'description': forms.Textarea()
        }
        field_args = {
            'img': {'required': False}
        }