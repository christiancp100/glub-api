from django.contrib import admin
from .models import Suggestion


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'user', 'event',)
