from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from src.apps.base.api.mixins import SerializerPerAction, PermissionPerAction
from src.apps.events.models import Event
from src.apps.events.api.serializers import (
    EventRegisterUnRegisterSerializer,
    EventSerializer,
)


class EventViewSet(SerializerPerAction, PermissionPerAction, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    action_serializers = {
        "default": EventSerializer,
        "register_on_event": EventRegisterUnRegisterSerializer,
        "unregister_on_event": EventRegisterUnRegisterSerializer,
    }
    action_permissions = {
        "default": (IsAuthenticated,),
        "list": (AllowAny,),
        "register_on_event": (IsAuthenticated,),
        "unregister_on_event": (IsAuthenticated,),
    }

    @action(methods=["GET"], detail=True)
    def register_on_event(self, request: Request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event)
        user = request.user
        if event.participants.contains(user):
            return Response("Вы уже участвуете в мероприятии")
        event.participants.add(user)
        return Response(
            [
                {"message": "Поздравляем! Вы участник мероприятия!"},
                serializer.data,
            ]
        )

    @action(methods=["DELETE"], detail=True)
    def unregister_on_event(self, request: Request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(event)
        user = request.user
        if event.participants.contains(user):
            return Response("Невозможно отменить участие!")
        event.participants.remove(user)
        return Response(
            [
                {"message": "Отмена регистрации прошло успешно!"},
                serializer.data,
            ]
        )
