from django import forms
from .models import Post
from django.utils.text import slugify

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['user', 'title', 'slug', 'image', 'content']
        
        labels = {
            'title': 'This is title',
            'slug': 'This is slug',
            'content': 'this is content',
            'image': 'This is image',
        }

        help_text = {  # this is used for django translation
            'title': 'This is title',
            'slug': 'This is slug',
            'content': 'this is content',
            'image': 'This is image',
        }

        error_messages = {
            "title": {
                "max_length": "This is too long.",
                "required": "The title field is required."
            },
            "slug": {
                "max_length": "This is too long.",
                "required": "The slug is required.",
                "unique": "This slug field must be unique bro",
            }
        }
    
    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        # self.fields['title'].error_messages = {
        #         "max_length": "This is too long.",
        #         "required": "The title field is required."
        #     }
        self.fields['content'].widget = forms.Textarea()

        for field in self.fields.values():
            field.error_message = {
                'required': 'you konw, {fieldname} is rquired'.format(fieldname=field.label),
            }

    def clean_title(self): # field level validation in django model form
        data = self.cleaned_data["title"]
        return slugify(data)
        

        
    