from django.views.generic.simple import direct_to_template

from timeline.models import Movie

def movies(request):
    movies = Movie.objects.all().order_by('-date_watched')
    return direct_to_template(request, 'base.html', {'movies': movies})
        