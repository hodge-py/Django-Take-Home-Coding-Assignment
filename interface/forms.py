from django import forms

class searchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100, required=False)
    category = forms.MultipleChoiceField(
        label='Category',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[]  # Choices will be set dynamically in the view
    )
    tags = forms.MultipleChoiceField(
        label='Tags',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[]  # Choices will be set dynamically in the view
    )