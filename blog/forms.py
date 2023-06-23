from django import forms

from .models import Tag, Article,Comment


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'created_at', 'category', 'tags',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'created_at', 'category', 'tags',)


class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)