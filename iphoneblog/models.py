from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget
from django.utils.text import slugify
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Smartphone(models.Model):
    """
    Model for smartphone
    """
    title = models.CharField(max_length=100, blank=True)
    smartphone_image = CloudinaryField("image", default="placeholder")
    slug = models.SlugField(max_length=100, unique=True, default="", null=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        verbose_name = "Smartphone"
        verbose_name_plural = "Smartphones"

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model for Author
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default="", unique=True)
    approved = models.BooleanField(default=False)
    author_image = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    iPhone_type = models.TextField(blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    comment_count = models.IntegerField(default=0)
    best_feature = models.CharField(
        max_length=150, verbose_name="Best feature of the smartphone"
        )
    battery_life = models.CharField(
        max_length=200, verbose_name="Average battery life")
    smartphones = models.ManyToManyField(Smartphone, blank=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + " | " + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title, allow_unicode=True)
    #     super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

