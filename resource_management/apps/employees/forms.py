import datetime
from django import forms

from apps.employees.models import Schedule


class ScheduleForm(forms.ModelForm):
    # This form is to batch create an employee's schedule.
    block_start = forms.DateField(initial=datetime.date.today)
    block_end = forms.DateField()
    sunday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    sunday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    monday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    monday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    tuesday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    tuesday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    wednesday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    wednesday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    thursday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    thursday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    friday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    friday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    saturday_shift_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    saturday_shift_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Schedule

        fields = ['employee']

