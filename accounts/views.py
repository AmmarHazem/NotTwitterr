from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm

from datetime import datetime


class Login(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('home')
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form' : form})

    def post(self, request):
        if request.user.is_authenticated():
            return redirect('home')
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user:
                user.profile.last_login = timezone.now()
                user.save()
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('home')
        print(form.errors)
        return render(request, 'accounts/login.html', {'form' : form})


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/sign-up.html', {'form' : form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username = cd['username'], password = cd['password1'], email = cd['email'])
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'registration/sign-up.html', {'form' : form})

