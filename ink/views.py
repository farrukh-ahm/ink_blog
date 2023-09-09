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


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post_detail = get_object_or_404(queryset, slug=slug)
        comments = post_detail.commented_post.all()
        context = {
            'post_detail': post_detail,
            'comments': comments
        }

        return render(request, 'post_detail.html', context)
