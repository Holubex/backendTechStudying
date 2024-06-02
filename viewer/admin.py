from django.contrib import admin
from viewer.models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Creator)