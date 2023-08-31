from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator

from django.urls import reverse_lazy

from django.views.generic.edit import DeleteView

from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import CommentForm, PostForm


# List of all posts
def post_list(request):
    posts = Post.objects.filter(status="published")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "post/list.html", {"page_obj": page_obj})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post/post_edit.html", {"form": form})


# Detail view on post
@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
            return render(
                request,
                "post/detail.html",
                {"post": post, "comments": comments, "comment_form": CommentForm()},
            )
    if request.method == "GET":
        comment_form = CommentForm()
    return render(
        request,
        "post/detail.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, "post/post_edit.html", {"form": form})


class BlogDeleteView(DeleteView):
    login_required = True
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("dashboard")
