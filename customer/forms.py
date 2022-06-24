

from dataclasses import field
from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        # mentioning this is for customer
        model = Customer
        # for mapping with db
        fields = "__all__"