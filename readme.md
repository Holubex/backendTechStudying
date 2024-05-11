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

## spustenie

spustime prikazom: `python manage.py runserver`

pokial chceme spustit viac serverov, tak mozeme zmenit port:
`python manage.py runserver 8001`