from django.contrib import admin
from .models import Bar, BarImages


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'id',)


@admin.register(BarImages)
class BarAdmin(admin.ModelAdmin):
    list_display = ('bar', 'image')
