from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, View, ListView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.models import LikeNotification
from .forms import TweetForm
from .models import Tweet, Like



class CreateTweet(FormView):
    model = Tweet
    form_class = TweetForm
    template_name = 'base.html'

    def form_invalid(self, form):
        tweets = self.request.user.profile.get_timeline()
        return render(self.request, 'base.html', {'tweet_form' : form, 'tweets' : tweets, 'error' : form.errors.get('__all__')})

    def form_valid(self, form):
        tweet = form.save(commit = False)
        tweet.user = self.request.user
        tweet.image = self.request.FILES.get('image')
        tweet.save()
        return redirect('home')


class LikeTweet(View):
    def post(self, request):
        if request.is_ajax():
            user = request.user
            tweet_id = request.POST.get('tweetId')
            tweet = get_object_or_404(Tweet, id = tweet_id)
            like_objects = tweet.like_set.all()
            users_liked_this_tweet = [like.user.id for like in like_objects]
            if user.id in users_liked_this_tweet:
                #dislike remove like object
                tweet.like_set.filter(user__id = user.id).delete()
                return JsonResponse({'unlike' : 'success', 'likes' : tweet.likes})
            else:
                # like create like object and create notification object
                Like.objects.create(tweet = tweet, user = user)
                like_notif = LikeNotification(source = user, destination = tweet.user, tweet = tweet)
                like_notif.content = f'{like_notif.source} liked your tweet.'
                like_notif.save()
                return JsonResponse({'like' : 'success', 'likes' : tweet.likes})
        print('NOT AJAX')
        return redirect(request.path)


