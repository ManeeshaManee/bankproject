from django import forms
from .models import Booking, City


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

        widgets = {
            'booking_date': DateInput(),
            'date_birth': DateInput(),
            'Gender': forms.RadioSelect(),

        }
        labels = {
            'date_birth': "DATE OF BIRTH",
            'u_name': "USERNAME",
            'age': "AGE",
            'Gender': "GENDER",
            'u_phone': "CONTACT NUMBER",
            'u_email': "EMAIL ADDRESS",
            'u_address': "HOME ADDRESS",
            # 'dic_name': "DISTRICT",
            # 'branch_name': 'BRANCH',
            'country': "DISTRICT",
            'city': 'BRANCH',
            'ac_type': 'ACCOUNT TYPE',
            'booking_date': 'DATE OF BOOKING',


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


