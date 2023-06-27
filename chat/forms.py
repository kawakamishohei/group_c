from django import forms
from .models import Chat, Comment


class ChatCreateForm(forms.ModelForm):

    class Meta:
        model = Chat
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('title','upname','text','created_at','category','image','tags',)

class ChatUpdateForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('title','text','created_at','category','tags',)

# class SearchForm(forms.Form):
#     keyword = forms.CharField(label='キーワード', required=False)

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','text',) # targetフィールドを含めない

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)
