from django.contrib import admin
from .models import *



def make_unverified(modeladmin, request, qs):
    qs.update(verified = False)

make_unverified.short_description = 'Mark selected profiles as unverified'

def make_verified(modeladmin, request, qs):
    qs.update(verified = True)

make_verified.short_description = 'Mark selected profiles as verified'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')
    list_display_links = ('user',)
    search_fields = ('slug', 'id')
    filter_horizontal = ('following',)
    list_filter = ('verified',)
    actions = [make_verified, make_unverified]

admin.site.register(Profile, ProfileAdmin)
