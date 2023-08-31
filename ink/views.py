from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from .models import *
from django.utils.text import slugify

class Home(generic.ListView):

    model = Post
    queryset = Post.objects.all()
    paginate_by = 9
    template_name = 'index.html'
