from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post/detail.html', {'post': post})


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
