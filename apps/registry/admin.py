from django.contrib import admin
from .models import Registry


@admin.register(Registry)
class BarAdmin(admin.ModelAdmin):
    list_display = ('date_registered', 'user', 'bar',)
