from typing import Any
from django import forms

class SearchForm(forms.Form):

    some_text = forms.CharField()
    boolean = forms.BooleanField()
    # email = forms.EmailField(min_length=10, initial='mizan@gmail.com') # setting intial value
    email = forms.EmailField(min_length=10)
    # integer = forms.IntegerField(initial=10) # setting intial value
    integer = forms.IntegerField()

    def __init__(self, user=None,*args, **kwargs): # setting intial value in the django form using __init__ method
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['some_text'].initial = 'New Text'
        self.fields['boolean'].initial = True
        self.fields['email'].initial = 'mizan@gmail.com'
        self.fields['integer'].initial = 333

        if user: # passing new text value from the views 
            self.fields['some_text'].initial = user

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get('integer')
        if integer < 10:
            raise forms.ValidationError('The integer must be greater than 10')
        # return 100
        return integer
        
    def clean_some_text(self, *args, **kwargs):
        some_text = self.cleaned_data.get('some_text')
        if len(some_text) <5:
            raise forms.ValidationError('The some text must be greater than 5')
            return some_text
