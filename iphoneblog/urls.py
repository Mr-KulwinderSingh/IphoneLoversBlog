from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('about', views.about, name="about"),
    path('all_models', views.all_models, name="all_models"),
    path('<slug:slug>', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('add_post', views.AddPost.as_view(), name="add_post")
]
