import os.path

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'timeline.views.movies', name="home"),
    url(r'^(?P<year>\d+)/?$', 'timeline.views.movies', name="timeline_movies"),
    # url(r'^timeline/', include('timeline.urls'), name="timeline"),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'assets')}),
    )