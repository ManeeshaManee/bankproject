from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

        widgets = {
            'booking_date': DateInput(),
            'date_birth': DateInput(),
        }
        labels = {
            'date_birth': "DATE OF BIRTH",
            'u_name': "USERNAME",
            'age': "AGE",
            'Gender': "GENDER",
            'u_phone': "CONTACT NUMBER",
            'u_email': "EMAIL ADDRESS",
            'u_address': "HOME ADDRESS",
            'dic_name': "DISTRICT",
            'branch_name': 'BRANCH',
            'ac_type': 'ACCOUNT TYPE',
            'booking_date': 'DATE OF BOOKING',

        }
