from django.db import models
from account.models import User

# Model for posts
class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250, verbose_name='Загаловок')
    slug = models.SlugField(
        max_length=250, unique_for_date="created", unique=True, verbose_name="URL"
    )
    author = models.ForeignKey(
        User, related_name="blog_posts", on_delete=models.CASCADE
    )
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft", verbose_name='Загаловок')

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title


# Model for comments
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return "Comment by {} on {}".format(self.name, self.post)
