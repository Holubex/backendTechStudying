import re
from concurrent.futures._base import LOGGER
from datetime import date

from django.core.exceptions import ValidationError
from django.db.models import TextField
from django.forms import Form, ModelChoiceField, CharField, IntegerField, DateField, Textarea, ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, FormView

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


def movies_by_rating(request):
    result = Movie.objects.all().order_by('rating', 'title')
    return render(request, 'movies_by_rating.html',
                  {'title': 'List of Movies by Rating',
                            'movies': result})

def genre(request, pk):
    if Genre.objects.filter(id=pk).exists():
        genre = Genre.objects.get(id=pk)
        items = Movie.objects.filter(genre=genre)
        return render(request, "genre.html", {'movies': items, 'genre': genre})

    return genres(request)


""" Class-Based Views """

# Prva verzia
# class MoviesView(View):
#
#     def get(self, request):
#         result = Movie.objects.all().order_by('title')
#         return render(request,
#                       template_name='movies.html',
#                       context={'title': 'List of Movies', 'movies': result})


# Druha verzia pomocou TemplateView - ked potrebujeme zadat len meno template a data
# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'title': 'List of Movies',
#                      'movies': Movie.objects.all().order_by('title')}

# Tretia moznost - kde definujeme len template a model a odkial sa beru data
class MoviesView(ListView):
    template_name = 'movies2.html'
    model = Movie

# class GenresView(TemplateView):
#     template_name = 'genres.html'
#     extra_context = {'title': 'List of Genres',
#                      'genres': Genre.objects.all().order_by('name')}

# class GenresView(View):
#
#     def get(self, request):
#         result = Genre.objects.all()
#         return render(request,
#                       template_name='genres.html',
#                       context={'genres': result})

class GenresView(ListView):
    template_name = 'genres2.html'
    model = Genre


class MoviesByRatingView(TemplateView):
    template_name = 'movies_by_rating.html'
    extra_context = {'title': 'List of Movies by Rating',
                     'movies': Movie.objects.all().order_by('-rating')}


""" Forms """
""" Validators """
def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')

class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(Form):
    title = CharField(max_length=64)
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = DateField()
    description = CharField(widget=Textarea, required=False)

    def clean_title(self):
        initial_data = super().clean()  # původní data ve formuláři od uživatele
        initial = initial_data['title']  # původní title od uživatele
        return initial.strip()  # odtraníme prázdné znaky na začátku a konci textu

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Commedy' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result


class MovieModelForm(ModelForm):

    class Meta:
        model = Movie       # z kterého modelu bude brát informace
        #fields = ['genre', 'title']  # které položky chceme ve formuláři zobrazit
        #exclude = ['description']    # které položky nechceme zobrazit
        fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def clean_title(self):
        initial_data = super().clean()  # původní data ve formuláři od uživatele
        initial = initial_data['title']  # původní title od uživatele
        return initial.strip()  # odtraníme prázdné znaky na začátku a konci textu

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Commedy' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movie_create')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description']
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
