from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "bar",
        "bar_id",
        "start_date",
        "finish_date",
        "is_active",
    )
