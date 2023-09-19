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
        else:
            add_post_form = PostForm()
        messages.success(request, "Post Added!")
        return redirect("/")


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post_detail = get_object_or_404(queryset, slug=slug)
        id = post_detail.id
        comments = post_detail.commented_post.all()
        comment_form = CommentForm()
        context = {
            'post_detail': post_detail,
            'id' : id,
            'comments': comments,
            'comment_form': comment_form,
            'is_True': True,
            'is_False': False,
        }

        return render(request, 'post_detail.html', context)

class PostComment(View):

    def post(self, request, slug, *args, **kwargs):
        print(f'SLUG: {slug}')
        try:
            post_find = Post.objects.get(slug=slug)
            print(post_find)
        except Post.DoesNotExist:
            print("Does not exist")
    
        # queryset = Post.objects.all()
        # post = get_object_or_404(queryset, slug=post_find.slug)

        comment_post = CommentForm(request.POST)
        print(f'ID: {post_find}')

        if comment_post.is_valid:
            comment = comment_post.save(commit=False)
            comment.commented_by = request.user
            comment.commented_post = post_find
            comment.approved = False

            comment.save()
        else:
            comment_post = CommentForm()
        
        return redirect(reverse('post_detail', args=[post_find.slug]))

class CommentApprove(View):

    def post(self, request, id, *args, **kwargs):
        comment = Comment.objects.get(id=id)
        post = comment.commented_post
        comment.approved = True
        comment.save()

        return redirect(reverse('post_detail', args=[post.slug]))

class CommentDelete(View):

    def post(self, request, id, *args, **kwargs):
        print("1st step")
        comment = Comment.objects.get(id=id)
        post = comment.commented_post
        comment.delete()

        return redirect(reverse('post_detail', args=[post.slug]))


class UserPosts(View):

    def get(self, request, *args, **kwargs):
        try:
            user_posts = Post.objects.filter(author=request.user)
            context = {
                'user_posts': user_posts,
            }
        except:
            context = {
                'user_posts': "Not Authorised"
            }

        return render(request, 'userposts.html', context)


# class PostEdit(View):
