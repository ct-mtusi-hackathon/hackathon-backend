from rest_framework import serializers

from src.apps.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "image",
            "start_date",
            "end_date",
            "location",
            "coins_for_registration",
            "coins_for_victory",
            "is_active",
        )
