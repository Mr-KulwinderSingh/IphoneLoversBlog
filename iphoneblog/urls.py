from . import views
from iphoneblog import views
from django.urls import path, include


from django.urls import path
from . import views

urlpatterns = [
    path("", views.Allsmartphone.as_view(), name="home"),
    path('about', views.about, name="about"),
    path('blog', views.AllBlogPost.as_view(), name="all-blog"),
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
    path(
        "smartphones_post/<str:sma>",
        views.smartphones_view,
        name="smartphones-post",
    ),
]
