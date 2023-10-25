from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=50, null=False, unique=True)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    excerpt = models.TextField(blank=False)
    content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now=True)
    edited_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes')
    featured_image = models.ImageField(upload_to='ink/', default='ink/ink_blot')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f'{self.author}: {self.title}'

    def likes_count(self):
        return self.likes.count()

    def user_like(self):
        like = self.likes.all()
        users = []
        for i in like:
            users.append(i.id)
        return users



class Comment(models.Model):
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented_by')
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commented_post')
    commented_text = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.commented_by}: {self.commented_text}'


class Subscribe(models.Model):
    subscriber = models.ManyToManyField(User, related_name='subscriber')
    sub_to = models.ManyToManyField(User, related_name='sub_to')

    def sub_count(self):
        return self.subscriber.count()

    def user_subs(self):
        subs = self.subscriber.all()
        users = []
        for i in like:
            users.append(i.id)
        return users

    def __str__(self):
        return f'{self.sub_to}: {self.subscriber}'
