from django import forms

class searchForm(forms.Form):
    search_query = forms.CharField(label='search', max_length=100, required=False)
    category = forms.MultipleChoiceField(
        label='category',
        choices=[('Video Game','Video Game'),('Book','Book'),('Music','Music'),('Tools','Tools'),('Homeware','Homeware')],
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    tags = forms.MultipleChoiceField(
        label='tags',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[('War', 'War'), ('Story', 'Story'), ('kitchen', 'kitchen')] 
    )