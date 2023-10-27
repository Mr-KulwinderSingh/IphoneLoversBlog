from . import views
from iphoneblog import views
from django.urls import path, include


from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('about', views.about, name="about"),
    path('all_models', views.all_models, name="all_models"),
    path('user_page', views.User.as_view(), name="user-page"),
    path('add_post', views.AddPost.as_view(), name="add-post"),
    path('<slug:slug>', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('update_post/<slug:slug>', views.update_post, name="update-post"),
    path(
        'user_post_list/', views.UserPostList.as_view(),
        name="user-post-list"),
    path(
        'delete_post/<slug:slug>',
        views.DeletePost.as_view(), name="delete-post"),
]
