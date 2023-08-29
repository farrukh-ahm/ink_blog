from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from .models import *
from django.utils.text import slugify

class Home(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')
