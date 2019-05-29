from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q, Max

from random import shuffle

from tweets.forms import TweetForm
from profiles.models import Profile
from notifications.models import LikeNotification


class Home(View):
    def get(self, request):
        tweets = None
        tweet_form = None
        profiles_qs = None
        cxt = {}
        if request.user.is_authenticated():
            tweets = request.user.profile.get_timeline()
            tweet_form = TweetForm()
            exclude_ids = [u.profile.id for u in request.user.profile.following.all()]
            ids = [p.id for p in Profile.objects.exclude(id__in = exclude_ids)]
            shuffle(ids)
            ids = ids[:3]
            profiles_qs = Profile.objects.filter(id__in = ids)
            cxt = {
                'tweets' : tweets,
                'tweet_form' : tweet_form,
                'who_to_follow' : profiles_qs,
                'notifications' : self.get_notifications()
            }
        return render(request, 'base.html', cxt)

    def get_notifications(self):
        return LikeNotification.objects.filter(destination = self.request.user)


class Search(View):
    def get(self, request):
        q = request.GET.get('q')
        if q:
            lookup_query = Q(slug__icontains = q) | Q(user__first_name__icontains = q) | Q(user__last_name__icontains = q)
            profile_qs = Profile.objects.filter(lookup_query).distinct()
            return render(request, 'search_result.html', {'profiles' : profile_qs, 'q' : q})
        return redirect(request.path)
