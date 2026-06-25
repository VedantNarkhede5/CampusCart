from django import forms
from .models import Product
from django import forms
from .models import Review
from .models import Order

class ConfirmOrderForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'meeting_location',
            'meeting_time'
        ]

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'title',
            'category',
            'description',
            'condition',
            'price',
            'image',
            'is_urgent'
        ]

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment']