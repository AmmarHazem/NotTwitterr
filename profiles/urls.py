from django.conf.urls import url
from .views import *

app_name = 'profiles'


urlpatterns = [

    url(r'^edit/$', UpdateProfile.as_view(), name = 'update'),
    # url(r'^(?P<slug>[-\w]+)/$', ProfileDetail.as_view(), name = 'profile'),
]