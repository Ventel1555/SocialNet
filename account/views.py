from django.shortcuts import render

from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.urls import reverse

from django.http import HttpResponseRedirect

from blog.models import Post

from account.models import User

from .forms import UserEditForm, UserRegistrationForm


# list of all your own posts
def dashboard(request, nickid=None):
    if nickid == None and request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)

        paginator = Paginator(posts, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "dashboard.html", {"page_obj": page_obj})
    else:
        usernick = get_user_model().objects.get(id=nickid)
        posts = Post.objects.filter(author=usernick, status="published")
        
        paginator = Paginator(posts, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "post/blogers.html", {"page_obj": page_obj, "usernick": usernick})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # Save the User object
            new_user.save()
            return render(
                request, "registration/register_done.html", {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Profile updated successfully")
            return render(request, "account/edit.html", {"user_form": user_form})
        else:
            messages.error(request, "Error updating your profile")
            return render(request, "account/edit.html", {"user_form": user_form})
    else:
        user_form = UserEditForm(instance=request.user)
        return render(request, "account/edit.html", {"user_form": user_form})


@login_required
def followToggle(request, author_id):
    authorObj = User.objects.get(id=author_id)
    currentUserObj = User.objects.get(id=request.user.id)
    following = authorObj.following.all()

    if author_id != currentUserObj.id:
        if currentUserObj in following:
            authorObj.following.remove(currentUserObj.id)
        else:
            authorObj.following.add(currentUserObj.id)

    return HttpResponseRedirect(reverse(dashboard, args=[authorObj.id]))