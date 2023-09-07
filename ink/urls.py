from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addpost/<str:user>', views.AddPost.as_view(), name='add_post'),
]