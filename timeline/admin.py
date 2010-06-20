from django.contrib import admin

from timeline.models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'location')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Location)