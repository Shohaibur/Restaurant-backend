from datetime import datetime, timedelta
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class reservation_form(forms.Form):
    user_name = forms.CharField(
        label="Full name",
        validators=[RegexValidator(regex='^[A-Z][a-zA-Z]{3,}$', message="Enter Valid Name")],
        widget=forms.TextInput(attrs={'placeholder': "Jane doe"})
    )

    CHOICES = [(str(i), str(i)) for i in range(1, 11)]

    guest_no = forms.ChoiceField(label="No. of Guests", choices=CHOICES)

    reservation_date = forms.DateField(
        label="Reservation Date",
        widget=forms.TextInput(attrs={'type': "date"})
    )
    reservation_time = forms.TimeField(
        label="Reservation time",
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    user_email = forms.EmailField(
        label="Email",
        validators=[RegexValidator(regex='^[a-zA-Z0-9._%+-]+@gmail\.com$', message="Please Enter valid email address")],
        widget=forms.TextInput(attrs={"placeholder": "example@gmail.com"})
    )

    special_req = forms.CharField(
        label="Special Requests",
        required=False,
        widget=forms.Textarea(attrs={'placeholder': "If Any", 'rows': 2})
    )

    user_phone_num = forms.CharField(
        label="Phone Number",
        validators=[RegexValidator(regex='^01[0-9]{9}$', message="Please enter valid phone number")],
        widget=forms.NumberInput(attrs={'placeholder': '01xxxxxxxxx'})
    )

    def clean(self):
        cleaned_data = super().clean()
        current_datetime = datetime.now()
        current_datetime_plus_six_hours = current_datetime + timedelta(hours=6)

        # Convert reservation date and time to datetime object
        reservation_datetime = datetime.combine(cleaned_data['reservation_date'], cleaned_data['reservation_time'])

        # Check if date is not in the past
        if cleaned_data['reservation_date'] < datetime.now().date():
            raise ValidationError("Reservation date cannot be in the past.")

        # Check if reservation is less than 6 hours from the current time
        if reservation_datetime < current_datetime_plus_six_hours:
            raise ValidationError("Reservation must be at least 6 hours from the current time.")

        # Check if reservation is at the same time or in the past
        if cleaned_data['reservation_date'] == datetime.now().date() and cleaned_data['reservation_time'] <= current_datetime.time():
            raise ValidationError("Reservation time cannot be in the past.")

        return cleaned_data
