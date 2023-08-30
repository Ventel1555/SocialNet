from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        body = forms.CharField(widget=forms.TextInput(attrs={"class": "form-label"}))
        fields = ("body",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "body", "status")
