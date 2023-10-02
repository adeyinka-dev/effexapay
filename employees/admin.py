from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeProfileForm, EmployeeRegistrationForm
from .models import Employee


class EmployeeAdmin(UserAdmin):
    add_form = EmployeeRegistrationForm
    form = EmployeeProfileForm
    model = Employee
    list_display = ["username", "email", "full_name", "mobile_number"]


admin.site.register(Employee, EmployeeAdmin)
