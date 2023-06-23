from django import forms
from .models import Timetable, Subject

class TimetableCreateForm(forms.ModelForm):

    class Meta:
        model = Timetable
        # fields = '__all__'
        fields = ('day','subject', 'text')
        # fields = ('day', 'subject', 'subject','subject','subject','subject','subject', 'text')

class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class TimetableUpdateForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ('day', 'subject', 'text')

