from django import forms

SOME_CHOCES = [
    ('db-value', 'Display Value'),
    ('db-value2', 'Display Value2'),
    ('db-value3', 'Display Value3'),
    ('db-value4', 'Display Value4'),
]

INIT_CHOICES = [tuple([x,x]) for x in range(1,102) ]
"""
The above line of code will produce value like this
[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), 
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), 
(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), 
(27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34),
(35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), 
(43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), 
(51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), 
(59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), 
(67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74),
(75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82),
(83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90),
(91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), 
(99, 99), (100, 100)]
"""

YEARS = [x for x in range(1980-2031)]

class SearchForm(forms.Form):

    date_field = forms.DateField(initial="2010-10-20",widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label='Text',widget=forms.Textarea(attrs={'rows':4, 'col':10}))
    choices = forms.CharField(label='Select',widget=forms.Select(choices=SOME_CHOCES)) # dropdown items and checkbox
    choices2 = forms.CharField(label='Radio Button',widget=forms.RadioSelect(choices=SOME_CHOCES))
    choices3 = forms.CharField(label='Checkbox',widget=forms.CheckboxSelectMultiple(choices=SOME_CHOCES))
    boolean = forms.BooleanField(label='Admin')
    # email = forms.EmailField(min_length=10, initial='mizan@gmail.com') # setting intial value
    email = forms.EmailField(min_length=10)
    # integer = forms.IntegerField(initial=10) # setting intial value
    integer = forms.IntegerField(widget=forms.Select(choices=INIT_CHOICES))

    def __init__(self, user=None,*args, **kwargs): # setting intial value in the django form using __init__ method
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['some_text'].initial = 'New Text'
        self.fields['boolean'].initial = True
        self.fields['email'].initial = 'mizan@gmail.com'
        self.fields['integer'].initial = 101

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
