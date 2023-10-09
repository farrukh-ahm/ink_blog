from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addpost/<str:user>', views.AddPost.as_view(), name='add_post'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('comment_approve/<int:id>', views.CommentApprove.as_view(), name='comment_approve'),
    path('comment_delete/<int:id>', views.CommentDelete.as_view(), name='comment_delete'),
    path('userposts/<str:user>', views.UserPosts.as_view(), name='user_posts'),
    path('userposts/post_edit/<str:user>/<slug:slug>', views.PostEdit.as_view(), name='post_edit'),
    path('post_delete/<slug:slug>', views.PostDelete.as_view(), name='postdelete'),
    path('post_detail/postlike/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_detail/postlike_index/<slug:slug>', views.PostLikeIndex.as_view(), name='post_like_index'),
    path('profile/<str:user>', views.UserProfile.as_view(), name='profile'),
]