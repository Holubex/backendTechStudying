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