from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Employee(AbstractUser):
    email = models.EmailField(null=True)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.PositiveBigIntegerField()
    bank = models.ForeignKey("banklist_api.Bank", on_delete=models.SET_NULL, null=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        # Validators to ensure account number is exactly 10 digits
        validators=[
            RegexValidator(
                regex="^\d{10}$",
                message="Account number must be exactly 10 digits",
                code="invalid_account_number",
            )
        ],
    )
