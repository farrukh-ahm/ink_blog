from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from .models import *
from .forms import *
from django.utils.text import slugify

class Home(generic.ListView):

    model = Post
    queryset = Post.objects.all().filter(status=1)
    paginate_by = 9
    template_name = 'index.html'


class AddPost(View):

    def get(self, request, *args, **kwargs):
        add_post_form = PostForm()
        context = {
            'add_post_form': add_post_form,
        }

        return render(request, 'add_post.html', context)

    def post(self, request, *args, **kwargs):
        add_post_form = PostForm(request.POST, request.FILES)

        if add_post_form.is_valid():
            new_post = add_post_form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(f'{request.user}-{new_post.title}')

            new_post.save()
        messages.success(request, "Post Added!")
        return redirect("/")

