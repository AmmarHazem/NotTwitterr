from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from tweets.models import Tweet

def avatar_loc(obj, filename):
    return '{user}/profile/avatars/'.format(user = obj.user) + filename

def cover_loc(obj, filename):
    return '{user}/profile/covers/'.format(user = obj.user) + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank = True)
    avatar = models.ImageField(upload_to = avatar_loc, null = True, blank = True)
    cover = models.ImageField(upload_to = cover_loc, blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(null = True, blank = True)
    birth_date = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 200, blank = True)
    following = models.ManyToManyField(User, related_name = 'follow')
    verified = models.BooleanField(default = False)
    slug = models.CharField(max_length = 100, blank = True)

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs = {'slug' : self.slug})

    def get_timeline(self):
        tweets = Tweet.objects.none()
        for user in self.following.all():
            tweets = tweets | user.tweet_set.all()
        return tweets.order_by('-created')

    @property
    def get_tweets(self):
        return self.user.tweet_set.all()

    @property
    def get_following(self):
        return self.following.exclude(id = self.user.id)

    @property
    def get_followers(self):
        return self.user.follow.exclude(id = self.id)

    @property
    def tweets_number(self):
        return self.user.tweet_set.count()

    @property
    def following_count(self):
        return self.following.exclude(id = self.user.id).count()

    @property
    def followers_count(self):
        return self.user.follow.exclude(user = self.user).count()

    @property
    def likes_number(self):
        return self.user.like_set.count()
