from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# Create your views here.
def index(request):

    # 最新的 post 在前面显示
    post_list = Post.objects.all().filter(is_delete=False).order_by('-created_time')

    context = dict(
        post_list=post_list,
    )

    return render(request, 'blog/index.html', context=context)
