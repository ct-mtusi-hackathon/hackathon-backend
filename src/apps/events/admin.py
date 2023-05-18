from django.contrib import admin

from src.apps.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
