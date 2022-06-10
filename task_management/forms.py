from django import forms

from .models import ToDo


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskToDoForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-field'}))
    additional_information = forms.CharField(label='Additional information',
                                             widget=forms.TextInput(attrs={'class': 'form-field'}))
    time_expiration = forms.DateField(label='Expires at', widget=DateInput)

    class Meta:
        model = ToDo
        fields = ('title', 'additional_information', 'time_expiration',)
