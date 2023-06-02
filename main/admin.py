from django.contrib import admin

from main.models import Musician, Song, Award

# Register your models here.
admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Award)