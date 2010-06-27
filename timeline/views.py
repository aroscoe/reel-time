from django.views.generic.simple import direct_to_template

from timeline.models import Movie

def movies(request, **kwargs):
    year = kwargs.get('year')
    if year:
        movies = Movie.objects.filter(date_watched__year=year).order_by('-date_watched')
    else:
        movies = Movie.objects.all().order_by('-date_watched')
    return direct_to_template(request, 'base.html', {'movies': movies})
        