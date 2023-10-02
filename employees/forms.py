from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Make email mandatory during registration

    class Meta:
        model = Employee
        fields = ("username", "email", "password1", "password2")


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "full_name",
            "mobile_number",
            "bank",
            "account_name",
            "account_number",
        ]
