from django.shortcuts import render
from .models import Post
# from django.utils.translation import gettext as _
from django.utils.translation import gettext as _
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'hello': _('Hello')
    }
    return render(request, 'index.html', context)
