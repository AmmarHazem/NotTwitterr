"""NotTwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from .views import Home, Search
from profiles.views import ProfileDetail, FollowingList, UserFollowing, FollowersList, UserFollowers, Follow, Unfollow, UserLikes, Likes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name = 'home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^tweet/', include('tweets.urls')),
    url(r'^search/$', Search.as_view(), name = 'search'),
    url(r'^follow/$', Follow.as_view(), name = 'follow'),
    url(r'^unfollow/$', Unfollow.as_view(), name = 'unfollow'),
    url(r'^following/$', UserFollowing.as_view(), name = 'user-following'),
    url(r'^followers/$', UserFollowers.as_view(), name = 'user-followers'),
    url(r'^likes/$', UserLikes.as_view(), name = 'user-likes'),
    url(r'^(?P<slug>[-\w]+)/$', ProfileDetail.as_view(), name = 'profile'),
    url(r'^(?P<profile>[-\w]+)/following/$', FollowingList.as_view(), name = 'following'),
    url(r'^(?P<profile>[-\w]+)/followers/$', FollowersList.as_view(), name = 'followers'),
    url(r'^(?P<profile>[-\w]+)/likes/$', Likes.as_view(), name = 'likes'),
    url(r'^profile/', include('profiles.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
