from django.contrib import admin
from FizzBuzz.models import FizzBuzz


@admin.register(FizzBuzz)
class FizzBuzzAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created', 'updated')
    list_display_links = ('__str__',)
