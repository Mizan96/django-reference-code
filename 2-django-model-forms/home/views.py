from django.shortcuts import render
from django.utils.text import slugify
from django.views import View

from .forms import PostModelForm

class HomeView(View):

    def get(self, request, *args, **kwargs):
        form = PostModelForm()
        return render(request, 'index.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PostModelForm(request.POST or None)
        if form.is_valid():
            
            # using slugify before saving data
            """
            obj = form.save(False)
            obj.slug = slugify(obj.title)
            obj.save()
            """
            
            # Signals to slugify title
            """
            obj = form.save(False)
            obj.slug = slugify(obj.title)
            obj.
            """
            # using slugify in the modelform
            form.save()
        
        if form.has_error: # Rendering form errror into the view
            print(form.errors.as_json())
            print(form.errors.as_text())
            print(form.errors.as_data)
            # print(dir(form.errors))
            # print(dir(form))
            print(form.non_field_errors())
            

        return render(request, 'index.html', {'form': form})

