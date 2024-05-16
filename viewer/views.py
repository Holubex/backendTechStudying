from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import *
# Create your views here.

# view definovana pomococu funkcie
def hello(request):
    return HttpResponse("Hello World!")

def hello2(request, s):
    return HttpResponse(f'Hello {s} world!')


#URL encoding
def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} world!')

def hello4(request):

    adjectives = ['great', 'wonderful', 'beautiful']
    context = {'adjectives': adjectives}
    return render(
        request, # predavame na dalsiu stranku request
        template_name="hello.html", # nazov súboru
        context=context # posielame data ako slovnik
    )

def hello5(request, s0):

    s1 = request.GET.get('s1', '')
    return render(
        request, template_name="hello.html",
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )

def home(request):
    return render(request, template_name='home.html')

def genres(request):
    result = Genre.objects.all()
    return render(request,
                  template_name='genres.html',
                  context={'genres': result})

def movies(request):
    result = Movie.objects.all()
    return render(request,
                  template_name='movies.html',
                  context={'title': 'List of Movies', 'movies': result})

def movie(request, id):
    result = Movie.objects.get(id=id)
    return render(request,
                  template_name='movie_by_id.html',
                  context={'title': result.title,'movie': result.description,
                           'year': result.released, 'rating': result.rating})