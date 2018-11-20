from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import UpdateView, DetailView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .forms import ProfileForm
from .models import Profile
from tweets.models import Tweet


class Likes(LoginRequiredMixin, ListView):
    template_name = 'profiles/likes.html'
    context_object_name = 'likes'

    def get_context_data(self, *args, **kwargs):
        context = super(Likes, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get('profile')
        context['profile'] = get_object_or_404(Profile, slug = slug)
        context['status_navbar_active'] = 4
        return context

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get('profile')
        return Tweet.objects.liked_by(get_object_or_404(User, username = slug))


class UserLikes(LoginRequiredMixin, ListView):
    template_name = 'profiles/likes.html'
    context_object_name = 'likes'

    def get_context_data(self, *args, **kwargs):
        context = super(UserLikes, self).get_context_data(*args, **kwargs)
        context['profile'] = self.request.user.profile
        context['owner'] = True
        context['status_navbar_active'] = 4
        return context

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        return Tweet.objects.liked_by(self.request.user)


class Unfollow(LoginRequiredMixin, View):
    def post(self, request):
        if request.is_ajax():
            slug = request.POST.get('slug')
            unfollow_user = get_object_or_404(User, username = slug)
            self.request.user.profile.following.remove(unfollow_user)
            data = {'status' : 'Success'}
            return JsonResponse(data, status = 200)
        print('Not AJAX')
        return redirect(request.path)


class Follow(LoginRequiredMixin, View):
    def post(self, request):
        if request.is_ajax():
            slug = request.POST.get('slug')
            follow_user = get_object_or_404(User, username = slug)
            profile = self.request.user.profile
            profile.following.add(follow_user)
            response_data = {'reponse' : 'Success'}
            return JsonResponse(response_data)
        print('Not AJAX')
        return redirect(request.path)


class UserFollowers(ListView):

    template_name = 'profiles/followers.html'
    context_object_name = 'followers'

    def get_context_data(self, **kwargs):
        context = super(UserFollowers, self).get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        context['owner'] = True
        context['status_navbar_active'] = 3
        return context

    def get_queryset(self):
        return self.request.user.profile.get_followers


class FollowersList(ListView):

    template_name = 'profiles/followers.html'
    context_object_name = 'followers'

    def get_context_data(self, **kwargs):
        context = super(FollowersList, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(slug = self.kwargs.get('profile'))
        context['status_navbar_active'] = 3
        return context

    def get_queryset(self):
        profile_slug = self.kwargs.get('profile')
        profile = get_object_or_404(Profile, slug = profile_slug)
        followers = profile.get_followers
        return followers


class UserFollowing(LoginRequiredMixin, ListView):

    template_name = 'profiles/following.html'
    context_object_name = 'following'

    def get_context_data(self, **kwargs):
        context = super(UserFollowing, self).get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        context['owner'] = True
        context['status_navbar_active'] = 2
        return context

    def get_queryset(self):
        profile = self.request.user.profile
        following = profile.get_following
        return following


class FollowingList(ListView):

    context_object_name = 'following'
    template_name = 'profiles/following.html'

    def get_context_data(self, **kwargs):
        context = super(FollowingList, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(slug = self.kwargs.get('profile'))
        context['status_navbar_active'] = 2
        return context

    def get_queryset(self):
        profile_slug = self.kwargs.get('profile')
        profile = get_object_or_404(Profile, slug = profile_slug)
        following = profile.get_following
        return following


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if self.request.user.is_authenticated and self.request.user.profile.slug == slug:
            return super(ProfileDetail, self).get_object()
        return get_object_or_404(Profile, slug = slug)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetail, self).get_context_data(*args, **kwargs)
        user = context['object'].user
        if self.request.user.is_authenticated() and self.request.user.profile == self.object:
            context['owner'] = True
        context['status_navbar_active'] = 1
        context['tweets'] = user.tweet_set.all()
        return context


class UpdateProfile(LoginRequiredMixin, UpdateView):

    def set_name(self, full_name, user):
        name = full_name.split()
        if name:
            first_name = name[0]
            user.first_name = first_name
            last_name = ''.join(name[1:])
            if last_name:
                user.last_name = last_name
            else:
                user.last_name = ''
        else:
            user.first_name = ''
            user.last_name = ''
        user.save()

    def get(self, request):
        user = request.user
        profile = user.profile
        data = {}
        data['bio'] = profile.bio
        request.FILES['avatar'] = profile.avatar
        request.FILES['cover'] = profile.cover
        if profile.birth_date:
            data['birth_date'] = profile.birth_date.strftime('%Y-%m-%d')
        data['location'] = profile.location
        data['name'] = user.get_full_name()
        form = ProfileForm(data, request.FILES)
        return render(request, 'profiles/update_profile.html', {'form' : form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            user = request.user
            cd = form.cleaned_data
            self.set_name(cd.get('name'), user)
            form.save()
            messages.success(request, 'Your profile was successfully updated.')
            return redirect('profiles:update')
        messages.error(request, 'Please fix the errors below.')
        return render(request, 'profiles/update_profile.html', {'form' : form})
