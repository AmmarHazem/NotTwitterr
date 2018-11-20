from django.conf.urls import url
from .views import *

app_name = 'tweet'


urlpatterns = [

    url(r'^create/$', CreateTweet.as_view(), name = 'create'),
    url(r'^like/$', LikeTweet.as_view(), name = 'like'),
]