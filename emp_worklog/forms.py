from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class worklogForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)