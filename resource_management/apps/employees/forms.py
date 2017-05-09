import datetime
from django import forms

from apps.employees.models import Schedule


class ScheduleForm(forms.ModelForm):
    # This form is to batch create an employee's schedule.
    block_start = forms.DateField(initial=datetime.date.today)
    block_end = forms.DateField()
    sunday_shift_start = forms.TimeField()
    sunday_shift_end = forms.TimeField()
    monday_shift_start = forms.TimeField()
    monday_shift_end = forms.TimeField()
    tuesday_shift_start = forms.TimeField()
    tuesday_shift_end = forms.TimeField()
    wednesday_shift_start = forms.TimeField()
    wednesday_shift_end = forms.TimeField()
    thursday_shift_start = forms.TimeField()
    thursday_shift_end = forms.TimeField()
    friday_shift_start = forms.TimeField()
    friday_shift_end = forms.TimeField()
    saturday_shift_start = forms.TimeField()
    saturday_shift_end = forms.TimeField()

    class Meta:
        model = Schedule

        fields = ['employee']

