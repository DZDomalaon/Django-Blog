from django.forms import ModelForm
from .models import Articles, ArticleComments
from django import forms

class AddArticleForm(forms.ModelForm):
    title = forms.CharField(label="Title", required=True)
    description = forms.CharField(label="Description")
    content = forms.Textarea()
    
    class Meta:
        model = Articles
        fields = ('title', 'description', 'content')


class EditArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'description', 'content')


class ArticleCommentsForm(forms.ModelForm):

    class Meta:
        model = ArticleComments
        fields = ('comment',)


class ArticleCommentsEditForm(forms.ModelForm):

    comment = forms.CharField(label="Description", widget=forms.Textarea(attrs={'cols': 10, 'rows': 20}))
    class Meta:
        model = ArticleComments
        fields = ('comment',)