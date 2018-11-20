from django.contrib import admin
from .models import *


class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user',)
    search_fields = ('user__username',)


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Retweet)
admin.site.register(Like)
