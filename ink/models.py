from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Subscribe(models.Model):
    subscriber = models.ManyToManyField(User, related_name='subscriber')
    sub_to = models.ManyToManyField(User, related_name='sub_to')

    # def sub_count(self):
    #     return self.subscriber.count()

    def user_subs(self):
        subs = self.subscriber.all()
        users = []
        for i in subs:
            users.append(i.id)
        return users

    def __str__(self):
        return f'{self.sub_to}: {self.subscriber}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    profile_pic = models.ImageField(upload_to='ink/', default='ink/profile_pic', null=True, blank=True)
    homepage_link = models.CharField(null=True, blank=True, max_length=100)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100) 
    linkedin_link = models.CharField(null=True, blank=True, max_length=100)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)

    def sub_count(self):
        return self.followed_by.count()
    
    def following(self):
        return self.follows.count()

    def __str__(self):
        return self.user.username

# Creating profile when user is created

# @receiver(post_save, sender=User) --> can either use the @receiver decorator or the post_save signal as below
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()
        # Have the user follow themselves
        # user_follow = Subscribe()
        # user_follow.save()
        # user_follow.subscriber.set([instance.id])
        # user_follow.sub_to.set([instance.id])
        # user_follow.save()

        user_profile.follows.add(user_profile.id)
        user_profile.save()

post_save.connect(create_profile, sender=User)


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



