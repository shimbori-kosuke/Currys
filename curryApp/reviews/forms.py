from django import forms

class SearchForm(forms.Form):
        keyword = forms.CharField(label='Search', max_length=100)