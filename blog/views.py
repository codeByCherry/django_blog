from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Post
import markdown

# Create your views here.
def index(request):

    # 最新的 post 在前面显示
    post_list = Post.objects.all().filter(is_delete=False).order_by('-created_time')

    context = dict(
        post_list=post_list,
    )

    return render(request, 'blog/index.html', context=context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.is_delete:
        return HttpResponse("This post has been deleted!")

    post.body = markdown.markdown(
        post.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    context = dict(
        post=post,
    )

    return render(request, 'blog/detail.html', context=context )
