from django import forms
from .models import Post , Homework

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('date','title', 'text')
class HomeworkCreateForm(forms.ModelForm):

    class Meta:
        model = Homework
        fields = ('image',)
