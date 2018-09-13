from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = dict(
        title='Welcome',
        content='Hi, here',
    )

    return render(request, 'blog/index.html', context=context)
