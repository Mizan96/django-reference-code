from typing import Any
from django.shortcuts import render

from django.views import View

from .forms import SearchForm
# Create your views here.

class HomeView(View):
    """
    Get User post data using django forms
    """
    def get(self, request, *args, **kwargs):
        # inittial_dic = {    # setting intial value of the forms
        # 'some_text': 'Text',
        # 'boolean': True,
        # # 'email': 'Email',
        # # 'integer': 0
        # }
        # form = SearchForm(initial=inittial_dic) # setting initial value into the form
        

        """
        passing new text value into the foem __init__ method as argument though it is not necessary. 
        But there is a way something like that.
        I am showing this options
        """
        # form = SearchForm(user=request.user) 
        form = SearchForm()
        return render(request, 'index.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
       
        form = SearchForm(data=request.POST or None)
        if form.is_valid():
            print(form.cleaned_data) # only input data will be printed
            print(form.cleaned_data.get('email')) # valid
            # print(form.cleaned_data['email']) # valid 
            # print(request.POST) # csrf_token and input data will be printed
            # print('.......', request.POST.get('email')) # valid
            # print('###########', request.POST['email']) # valid
        return render(request, 'index.html', {'form': form})
