from django.contrib import admin
from .models import Post, Smartphone, Comment, Author
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    """
    Add fields for smartphone in admin panel
    """

    list_display = ("title", "slug", "excerpt")
    search_fields = ["title"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Add fields for the author in the admin panel
    """

    list_display = ("user", "email", "created_on", "approved")
    search_fields = ["user"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
