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