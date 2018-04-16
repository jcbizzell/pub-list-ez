from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('author_str', 'year', 'title', 'journal', \
            'other_str', 'doi', 'pubmed', 'citedby', 'keyword_str')

class SearchResultsForm(forms.Form):
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
