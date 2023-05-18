from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from src.apps.base.api.mixins import SerializerPerAction
from src.apps.events.models import Event
from src.apps.events.api.serializers import EventSerializer


class EventViewSet(SerializerPerAction, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    action_serializers = {
        "default": EventSerializer,
        "register_on_event": None,
    }

    @action(methods=["GET"], detail=True)
    def register_on_event(self, request: Request, *args, **kwargs):
        event = self.get_object()
        user = request.user
        if event.participants.contains(user):
            return Response("Вы участвуете в мероприятии")
        event.participants.add(user)
        return Response("Поздравляем! Вы участник мероприятия!")
