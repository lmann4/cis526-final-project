from datetime import timedelta, date
from django import forms

from apps.employees.models import Employee, Schedule


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


class ScheduleForm(forms.Form):
    # This form is to batch create an employee's schedule.
    employee = forms.ModelChoiceField(queryset=Employee.objects.filter(user__is_active=True), required=True)
    block_start = forms.DateField(initial=date.today, required=True)
    block_end = forms.DateField(required=True)
    sunday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    sunday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    monday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    monday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    tuesday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    tuesday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    wednesday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    wednesday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    thursday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    thursday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    friday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    friday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    saturday_shift_start = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))
    saturday_shift_end = forms.TimeField(input_formats=('%I:%M %p', '%I:%M'), widget=forms.TimeInput(format='%H:%M'))

    def clean(self):
        cleaned_data = super(ScheduleForm, self).clean()

        for date in daterange(cleaned_data['block_start'], cleaned_data['block_end']):
            if date.weekday() == 6 and cleaned_data.get('sunday_shift_start', None) and cleaned_data.get('sunday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['sunday_shift_start'],
                    end_time=cleaned_data['sunday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )
            elif date.weekday() == 0 and cleaned_data.get('monday_shift_start', None) and cleaned_data.get('monday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['monday_shift_start'],
                    end_time=cleaned_data['monday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )
            elif date.weekday() == 1 and cleaned_data.get('tuesday_shift_start', None) and cleaned_data.get('tuesday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['tuesday_shift_start'],
                    end_time=cleaned_data['tuesday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )
            elif date.weekday() == 2 and cleaned_data.get('wednesday_shift_start', None) and cleaned_data.get('wednesday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['wednesday_shift_start'],
                    end_time=cleaned_data['wednesday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )
            elif date.weekday() == 3 and cleaned_data.get('thursday_shift_start', None) and cleaned_data.get('thursday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['thursday_shift_start'],
                    end_time=cleaned_data['thursday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )
            elif date.weekday() == 4 and cleaned_data.get('friday_shift_start', None) and cleaned_data.get('friday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['friday_shift_start'],
                    end_time=cleaned_data['friday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )
            elif date.weekday() == 5 and cleaned_data.get('saturday_shift_start', None) and cleaned_data.get('saturday_shift_end', None):
                Schedule.objects.create(
                    date=date,
                    start_time=cleaned_data['saturday_shift_start'],
                    end_time=cleaned_data['saturday_shift_end'],
                    employee=cleaned_data['employee'],
                    employee_sub=None,
                    up_for_sub=0
                )

