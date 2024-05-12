# Django

## instalacia
Django nainstalujeme prikazom: 

`python -m pip install django==4.1.1`

Dolezite: kazdy v time musi mat taku istu verziu.

## vytvorenie projektu
vytvorime novy projekt prikazom:
`django-admin startproject hollymovies .`

V `.\hollymovies\settings.py` mame nastavienia

V `.\hollymovies\path.py` mame nastavene cesty

## GitHub 

nasledne zverejnit projekt na GitHub -> pozvat ostatnych clenov timu

## spustenie

spustime prikazom: `python manage.py runserver`

pokial chceme spustit viac serverov, tak mozeme zmenit port:
`python manage.py runserver 8001`

## zoznam nainstalovanych modulov 
`pip freeze > requirements.txt`

## vytvorenie aplikacie 
`python manage.py startapp viewer`

- migration -- zlozka, ktora obsahuje migracie
- admin.py -- administracna cast
- apps.py -- nastavenia aplikacie (bez zmien)
- models.py -- tu su definovame modely (tabulky databaze)
- tests.py -- tu riesime testy 
- views.py --  tu bude logika  (prepojenie na databaze a template)

### registrtacia aplikacie

Aplikacie musime zaregristrovat v subore `.\hollymovies\settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viewer'
]
```
## ORM 

Moodely vytvarame v subore `models.py` v doanej aplikaci.

## WARNING: Po kazdej zmene v modeloch (tj. v subore `models.py`) musime migrovat databzu

- vytcorenie migracneho skriptu: `python manage.py makemigrations`
- aplikuj migraciu: `python manage.py migrate`

WARNING: Migracne scripty vkladame do repozitara ale databazu nie (databaza moze obsahovat citlive udaje)

## shell 

Pre rychlu pracou s databazou mozeme vyuzit `python manage.py shell`

## Vytvorenie superuzivatela (admin)
`python manage.py createsuperuser`

http://127.0.0.1:8000/admin/ je administracny panel 

## export dat
`python manage.py dumpdata viewer --output fixtures.json`
kde 'viewer' je nazov aplikacie, z ktorej ezportujem data
data sa ulozia vo formate json

nasledne import dat z formatu json do databaza
`python manage.py loaddata fixtures.json`

WARNING: pri importe dat pozor na id (pk), pretoze sa do databaze vlozi s tymito id a prepisu original data

## Queries

### .get()
Vracia jednu instanciu najdeneho zaznamu v databazi.

### .filter()
Vracia zoznam instancii najdenych zaznamov.
`Movie.objects.filter(genre__name='Drama')`
`Movie.objects.filter(released__year=1994)`
`Movie.objects.filter(rating=5)`
`Movie.objects.filter(rating__gt=3)` `__gt` => vacsie nez
`Movie.objects.filter(rating__gte=3)` `__gte` => vacsie rovno
`Movie.objects.filter(rating__lt=3)` `__lt` => mensie nez
`Movie.objects.filter(rating__lte=3)` `__lte` => mensie rovno
`Movie.objects.filter(title="The Green Mile")`
`Movie.objects.filter(title__icontains="Green")` obsahuje 'Green'
`Movie.objects.exclude(released__year=1994)` filmy ktore neboli natocene v roku 1994
`Movie.objects.exclude(released__year=1994).exists()` vrati mi boolean ci existuje
`Movie.objects.exclude(released__year=1994).count()` COUNT prikaz (spocita zaznamy)
`Movie.objects.all().order_by('released')` ORDER BY prikaz
`Movie.objects.all().order_by('-released')` ORDER BY prikaz zostupne

## Data manipulation

### CREATE
`Genre.objects.create(name='Documentary')`

python
```
genre = Genre(name='Comedy')
genre.save()
```

### UPDATE 

`Movie.objects.filter(released__year=2000).update(rating=5)`

python
```
pulp_fiction = Movie.objects.get(title='Pulp Fiction')
pulp_fiction.rating = 7
pulp_fiction.save()
```

### DELETE
`Movie.objects.filter(title__contains='Godfather').delete()`