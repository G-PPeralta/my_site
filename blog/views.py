from django.shortcuts import get_object_or_404, render

from .models import Author, Post, Tag


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identifiede_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post-detail.html",
        {"post": identifiede_post, "post_tags": identifiede_post.tags.all()},
    )
