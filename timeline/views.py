from django.shortcuts import render_to_response

from timeline.models import Movie

def movies(request):
    movies = Movie.objects.all()
    return render_to_response('base.html', {'movies': movies})
        