from django import forms

class searchForm(forms.Form):
    search_query = forms.CharField(label='search', max_length=100, required=False)
    category = forms.MultipleChoiceField(
        label='category',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[]  # Choices will be set dynamically in the view
    )
    tags = forms.MultipleChoiceField(
        label='tags',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[]  # Choices will be set dynamically in the view
    )