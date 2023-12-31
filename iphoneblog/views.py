from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddPostForm, UpdatePostForm
from .forms import CommentForm
from django.template.defaultfilters import slugify


class Allsmartphone(generic.ListView):
    """
    Render all the smartphones on home page
    """
    model = Smartphone
    template_name = "index.html"


class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 9


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *argus, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
                },
        )

    def post(self, request, slug, *argus, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
                },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add a blog post only when user is logged in
    """
    model = Post
    form_class = AddPostForm
    template_name = "add_post.html"
    success_message = "You have added a new post, It's awaiting approval!"

    def get_success_url(self):
        """
        Set the reverse url for the successful addition
        of the post to the database
        """
        return reverse("user-page")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.slug = slugify(form.instance.title)
        return super().form_valid(form)


class UserPostList(LoginRequiredMixin, generic.ListView):
    """
    Any user can have a look all of their posts
    """
    model = Post
    author = Post.author
    template_name = "user_post_list.html"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(
            author=self.request.user, status=1).order_by(
            "-created_on") 


@login_required()
def update_post(request, slug):
    """
    User can update the post he had created
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        if request.method == "POST":
            form = UpdatePostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(
                    request, "Your post has been updated successfully")
                return redirect(reverse("user-post-list"))
            else:
                messages.error(request, "Failed to update the post")
        else:
            form = UpdatePostForm(instance=post)
    else:
        messages.error(request, "Sorry this is not your post")

    template = ('update_post.html',)
    context = {"form": form, "post": post}
    return render(request, template, context)


class DeletePost(DeleteView):
    """
    Class that will allow user to delete a post that he posted
    """
    model = Post
    template_name = "delete_post.html"
    success_message = "Post has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        To set the reverse url for the
        successfull deletion of the post
        """
        return reverse("user-post-list")


def about(request):
    """
    Render the about page
    """
    return render(request, "about.html")


def all_models(request):
    """
    Render the food page
    """
    return render(request, "all_models.html")


class User(LoginRequiredMixin, generic.ListView):
    """
    This will render the user page
    """

    model = Post
    template_name = "user_page.html"


def smartphones_view(request, sma):
    """
    Render the posts for selected smartphones
    """
    smartphones_post = Post.objects.filter(
        smartphones__title__contains=sma, status=1
    )
    return render(
        request,
        "smartphones_post.html",
        {"sma": sma.title(), "smartphones_post": smartphones_post},
    )


def smartphones_list(request):
    """Return a list of smartphones for the dropdown in the navbar"""
    smartphones_list = Smartphone.objects.all()
    context = {
        "smartphones_list": smartphones_list,
    }
    return context
