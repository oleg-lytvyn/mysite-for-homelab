from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
#
from .models import Post


def post_list(request):
    #
    posts_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(posts_list, 3) # 3 posts in each page
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )


# def post_detail(request):
#     post = get_object_or_404(
#         Post,
#         id=id
#     )
#     return render(
#         request,
#         'blog/post/post_detail.html',
#         {'post': post}
#     )
