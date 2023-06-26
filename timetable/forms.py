from django import forms
from .models import Timetable, Subject, Lunchmenu

class DateInput(forms.DateInput):
    input_type='date'

class TimetableCreateForm(forms.ModelForm):

    class Meta:
        model = Timetable
        # fields = '__all__'
        # fields = ('day','subject', 'text')
        # fields = ('day', 'subject', 'subject','subject','subject','subject','subject', 'text')
        fields = ('day', 'FirstPeriod', 'SecondPeriod', 'ThirdPeriod', 'FourthPeriod', 'FifthPeriod',
                  'SixthPeriod', 'text')
        widgets = {
            'day': DateInput()
        }

class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class TimetableUpdateForm(forms.ModelForm):
    class Meta:
        model = Timetable
        # fields = ('day', 'subject', 'text')
        fields = '__all__'

class LunchmenuCreateForm(forms.ModelForm):
    class Meta:
        model = Lunchmenu
        fields = '__all__'
        widgets = {
            'day': DateInput()
        }



