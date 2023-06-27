from django import forms

from .models import Tag, Kiji,Comment


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class KijiCreateForm(forms.ModelForm):
    class Meta:
        model = Kiji
        fields = ('title', 'text', 'created_at', 'category', 'tags',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','text',)


class KijiUpdateForm(forms.ModelForm):
    class Meta:
        model = Kiji
        fields = ('title', 'text', 'created_at', 'category', 'tags',)


class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)