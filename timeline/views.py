from django.views.generic.simple import direct_to_template

from timeline.models import Movie

def movies(request):
    movies = Movie.objects.all()
    return direct_to_template(request, 'base.html', {'movies': movies})
        