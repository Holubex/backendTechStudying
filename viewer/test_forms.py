from django.test import TestCase
from viewer.models import *
from viewer.views import GenreModelForm, MovieModelForm
import datetime


class GenreFormTest(TestCase):

    def test_genre_form_is_valid(self):
        form = GenreModelForm(
            data={'name': '   comedy   '}
        )
        print(f'test_genre_form_is_valid: {form.data}')
        self.assertTrue(form.is_valid())


class MovieFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title="The best movie",
            title_cz="Najlepsi film",
            rating=3,
            released=datetime.date(year=2020, month=1, day=1),
            length=123,
            description='Popis filmu',
        )
        genre_drama = Genre.objects.create(name='Drama')
        genre_comedy = Genre.objects.create(name='Comedy')
        country_cz = Country.objects.create(name='Czechia')
        country_sk = Country.objects.create(name='Slovak')
        movie.genres.add(genre_drama)
        movie.genres.add(genre_comedy)
        director1 = Creator.objects.create(
            name='Jano',
            surname='Mrkva',
            birth_date=date.today(),
            birth_place='Czechia',
            country=country_sk,
            sex=Sex.MAN,
            biography='Biography',
        )
        actor1 = Creator.objects.create(
            name='Zuzana',
            surname='Mrkvova',
            birth_date=date.today(),
            birth_place='Slovak',
            country=country_cz,
            sex=Sex.WOMAN,
            biography='Biography',
        )

    def test_movie_form_is_valid(self):
        form = MovieModelForm(
            data={
                'title': 'Nazov filmu',
                'title_cz': 'Najlepsi film',
                'genres': ['1'],
                'countries': ['2'],
                'directors': ['1', '2'],
                'actors': ['3', '4'],
                'rating': '3',
                'released': '2020-05-08',
                'length': '123',
                'description': 'Popis filmu',
                'clicked': '2',
            }
        )
        print(f'test_movie_form_is_valid: {form.data}')
        self.assertTrue(form.is_valid())

    