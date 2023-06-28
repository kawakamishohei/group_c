from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Timetable, Subject

class DateInput(forms.DateInput):
    input_type='date'

class TimetableCreateForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = '__all__'
        # fields = ('day','subject', 'text')
        # fields = ('day', 'subject', 'subject','subject','subject','subject','subject', 'text')
        # fields = ('day', 'FirstPeriod', 'SecondPeriod', 'ThirdPeriod', 'FourthPeriod', 'FifthPeriod',
        #           'SixthPeriod', 'text')
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

# class LunchmenuCreateForm(forms.ModelForm):
#     class Meta:
#         model = Lunchmenu
#         fields = ('image', 'menu', 'explain')

class TimetableSearchForm(forms.Form):
    day = forms.DateField(label='日付', required=False)

class YearMonthForm(forms.Form):
    year = forms.IntegerField()
    month = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])





