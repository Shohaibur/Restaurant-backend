from django import forms


class reservation_form(forms.Form):
    user_name = forms.CharField(label="Full name", widget=forms.TextInput(attrs={'placeholder': "Jane doe"}))
    user_email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"placeholder": "example@gmail.com"}))
    reservation_date = forms.DateField(
        label="Reservation Date",
        widget=forms.TextInput(attrs={'type': "date"})
    )
    reservation_time = forms.TimeField(
            label="Reservation time",
            widget=forms.TimeInput(attrs={'type': 'time'})
        )

