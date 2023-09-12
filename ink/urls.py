from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addpost/<str:user>', views.AddPost.as_view(), name='add_post'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('comment_approve/<int:id>', views.CommentApprove.as_view(), name='comment_approve'),
]