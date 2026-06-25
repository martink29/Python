from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by("-id")
    return render(request, "posts/post_list.html", {"posts": posts})