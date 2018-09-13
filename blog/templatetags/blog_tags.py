# 编写自定义标签 {% get_recent_posts as recent_post_list %}
from ..models import Post
from ..models import Category

from django import template


register = template.Library()

# 这里处理编写 get_recent_posts 函数，其他都是套路
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]




'''
这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义，
一个是 created_time ，即 Post 的创建时间，month 是精度，
order='DESC' 表明降序排列（即离当前越近的时间越排在前面）。
例如我们写了 3 篇文章，分别发布于 2017 年 2 月 21 日、2017 年 3 月 25 日、
2017 年 3 月 28 日，那么 dates 函数将返回 2017 年 3 月 和 2017 年 2 月这样一个时间列表，
且降序排列，从而帮助我们实现按月归档的目的。
:return: 
'''
@register.simple_tag
def archives():
    # >>> Post.objects.dates('created_time', 'day', order="DESC")
    # <QuerySet [datetime.date(2018, 9, 13)]>
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
