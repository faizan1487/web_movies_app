from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'language','img', 'userRating','mpaaRatingType','mpaaRatingLabel')
    search_fields = ('name', 'language')
    
    

