from django.test import TestCase
import datetime
from viewer.models import *

class MovieModelTest(TestCase):

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
        movie.genres.add(genre_drama)
        movie.genres.add(genre_comedy)
        country_cz = Country.objects.create(name='Czechia')
        country_sk = Country.objects.create(name='Slovak')
        movie.countries.add(country_cz)
        movie.countries.add(country_sk)
        director1 = Creator.objects.create(
            name='Jano',
            surname='Mrkva',
            birth_date=date.today(),
            birth_place='Czechia',
            country=country_sk,
            sex=Sex.MAN,
            biography='Biography',
        )
        movie.directors.add(director1)
        actor1 = Creator.objects.create(
            name='Zuzana',
            surname='Mrkvova',
            birth_date=date.today(),
            birth_place='Slovak',
            country=country_cz,
            sex=Sex.WOMAN,
            biography='Biography',
        )
        movie.actors.add(actor1)
        movie.save()

    def setUp(self):
        print('\n-'*8)

    def test_movie_str(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.__str__(), 'The best movie (2020)')
        print(f'test movie: {movie.title}')

    def test_title(self):
        movie = Movie.objects.get(id=1)
        print(f'test title: {movie.title}')
        self.assertEqual(movie.title, 'The best movie')

    def test_movie_actors(self):
        movie = Movie.objects.get(id=1)
        number_of_actors = movie.actors.count()
        print(f'test number of actors: {number_of_actors}')
        self.assertEqual(number_of_actors, 1)

