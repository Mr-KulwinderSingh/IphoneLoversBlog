from .models import Post
from .models import Comment
from django import forms


class AddPostForm(forms.ModelForm):
    """
    A form that will be used by the user to add a post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "featured_image",
            
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "hidded"
                }
            ),
            "content": forms.TextInput(
                attrs={"class": "form-control"}
            )
        }

          
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)