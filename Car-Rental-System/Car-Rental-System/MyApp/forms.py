#MyApp/forms.py
# from django import forms
from.models import Booking

class RentalForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_date', 'return_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'] = forms.CharField(max_length=100, initial=self.instance.customer.username)
        self.fields['customer_phone'] = forms.CharField(max_length=15)

    def save(self, commit=True):
        booking = super().save(commit=False)
        booking.customer.username = self.cleaned_data['customer_name']
        booking.customer.phone = self.cleaned_data['customer_phone']
        if commit:
            booking.save()
        return booking
