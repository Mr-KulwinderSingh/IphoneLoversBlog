from django_summernote.widgets import SummernoteWidget
from .models import Post
from .models import Comment
from django.forms import ModelForm
from django import forms


class AddPostForm(forms.ModelForm):
    """
    A form that will be used by the user to add a post
    """

    class Meta:
        model = Post
        fields = (
           "title",
           "smartphones",
           "content",
           "featured_image",
           "best_feature",
           "battery_life",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "hidded"
                }
            ),
            "smartphones":  forms.Select(attrs={"class": "form-control"}),
            "content": SummernoteWidget(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add your content here",
                }
            ),
            "best_feature": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add the feature you like",
                }
            ),
            "battery_life": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": " Number of hours in a normal use)",
                }
            ),
        }


class UpdatePostForm(forms.ModelForm):
    """
    This is the form to edit the blog post 
    """

    class Meta:
        model = Post
        fields = (
               "title",
               "smartphones",
               "content",
               "featured_image",
               "best_feature",
               "battery_life",
                )

    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "smartphones": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(attrs={"class": "form-control"}),
        "best_feature": forms.TextInput(attrs={"class": "form-control"}),
        "battery_life": forms.TextInput(attrs={"class": "form-control"}),
    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)