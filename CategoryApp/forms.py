from django import forms
from django.core import validators


class reservation_form(forms.Form):
    user_name = forms.CharField(label="Full name",
                                widget=forms.TextInput(attrs={'placeholder': "Jane doe"}),
                                validators=[validators.MinLengthValidator(3,
                                                                          message="Name must consist of min 3 letters")])

    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
               ('9', '9'), ('10', '10')]

    guest_no = forms.CharField(label="No. of Guests", widget=forms.Select(choices=CHOICES))

    reservation_date = forms.DateField(
        label="Reservation Date",
        widget=forms.TextInput(attrs={'type': "date"}),
    )
    reservation_time = forms.TimeField(
        label="Reservation time",
        widget=forms.TimeInput(attrs={'type': 'time'}))

    user_email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"placeholder": "example@gmail.com"}))

    special_req = forms.CharField(label="Special Requests", required=False,
                                  widget=forms.Textarea(attrs={'placeholder': "If Any", 'rows': 2}))

    user_phone_num = forms.CharField(label="Phone Number",
                                     widget=forms.NumberInput(attrs={'placeholder': '01xxxxxxxxx'}))
