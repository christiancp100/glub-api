from django.contrib import admin

from .models import Bar, BarImage


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "id",
    )


@admin.register(BarImage)
class BarImageAdmin(admin.ModelAdmin):
    list_display = ("bar", "image")
