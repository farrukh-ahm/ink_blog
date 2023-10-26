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

    def get(self, request, user, *args, **kwargs):
        try:
            user_posts = Post.objects.filter(author=request.user)
            print(user)
            context = {
                'user_posts': user_posts,
            }
        except:
            context = {
                'user_posts': "Not Authorised"
            }

        return render(request, 'userposts.html', context)


class PostEdit(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.get(slug=slug)
        edit_form = PostForm(instance=queryset)
        context = {
            'post': queryset,
            'edit_form': edit_form
        }

        return render(request, 'post_edit.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.get(slug=slug)
        edit_form = PostForm(request.POST, request.FILES, instance=queryset)

        if edit_form.is_valid:

            edit_details = edit_form.save(commit=False)
            edit_details.author = request.user
            edit_details.slug = slugify(f'{request.user}-{edit_details.title}')
            edit_details.save()

            return redirect(reverse('post_detail', args=[edit_details.slug]))
        
        else:
            edit_form = PostForm()

            return redirect(reverse('post_detail', args=[slug]))


class PostDelete(View):

    def post(self, request, slug, *args, **kwargs):
        post = Post.objects.get(slug=slug)
        post.delete()

        return redirect(reverse('user_posts', args=[request.user]))


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):

        post = Post.objects.get(slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(reverse('post_detail', args=[slug]))



class PostLikeIndex(View):

    def post(self, request, slug, *args, **kwargs):

        post = Post.objects.get(slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(reverse('home'))


class UserProfile(View):

    def get(self, request, user, *args, **kwargs):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=user)

        # Get all posts by the user
        posts = Post.objects.filter(author=user)
        posts_count = posts.count()

        # Get the sub list of the user
        subscribers = Subscribe.objects.get(sub_to=user)

        subbed = user.subscriber.count()

        # Get the profile set
        profile = Profile.objects.get(user=user)

        context = {
            'user': user,
            'posts': posts_count,
            'subscribers': subscribers,
            'subbed': subbed,
            'profile': profile,
        }
        
        return render(request, 'profile.html', context)


class UserFollow(View):

    def post(self, request, user, *args, **kwargs):

        queryset_user = User.objects.all()
        user_current = get_object_or_404(queryset_user, username=user)

        try:
            queryset_subb = Subscribe.objects.get(sub_to=user_current)
            if queryset_subb.subscriber.filter(id=request.user.id).exists():
                queryset_subb.subscriber.remove(request.user)
                print("remove")
            else:
                queryset_subb.subscriber.add(request.user)
                print("Add try block")
        
        except:
            print("leaving")
            subscription = Subscribe()
            subscription.save()
            subscription.subscriber.set([request.user])
            subscription.sub_to.set([user_current])
            subscription.save()
            print("check")


        # Getting Subscribers List

        subscribers = Subscribe.objects.get(sub_to=user_current)
        subbed = user_current.subscriber.count()


        # Getting Post list

        posts = Post.objects.filter(author=user_current.id)
        posts_count = posts.count()
        
        context = {
            'user': user,
            'posts': posts_count,
            'subscribers': subscribers,
            'subbed': subbed,
        }

        return redirect(reverse('profile', args=[user]))

