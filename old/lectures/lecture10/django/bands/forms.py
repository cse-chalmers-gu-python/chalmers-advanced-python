from django import forms

class BandSearchForm(forms.Form):
    query = forms.CharField(max_length=100, label="Query", required=False)
