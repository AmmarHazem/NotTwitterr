from django.db import models
from django.contrib.auth.models import User


def tweet_image_loc(obj, filename):
    return '{user}/tweets_media/'.format(user = obj.user) + filename


class TweetManager(models.Manager):
    def liked_by(self, user):
        likes = Like.objects.filter(user = user)
        liked_tweets = self.get_queryset().filter(id__in = [like.tweet.id for like in likes])
        return liked_tweets


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length = 256, blank = True)
    image = models.ImageField(upload_to = tweet_image_loc, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)

    objects = TweetManager()

    def __str__(self):
        return str(self.id)

    @property
    def tweet_user(self):
        return str(self.user)

    @property
    def likes(self):
        return self.like_set.count()

    def users_liked(self):
        likes = self.like_set.all()
        users = [like.user.id for like in likes]
        return users

    class Meta:
        ordering = ('-created', 'text')


class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'Tweet: {id}, User: {user}'.format(user = self.user, id = self.tweet.id)

    class Meta:
        ordering = ('-created',)


class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    tweet = models.ForeignKey(Tweet, null = True, blank = True, on_delete = models.SET_NULL)
    text = models.CharField(max_length = 256)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.user)
