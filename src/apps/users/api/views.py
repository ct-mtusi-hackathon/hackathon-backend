from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from src.apps.users.models.users import User
from src.apps.base.api.mixins import PermissionPerAction, SerializerPerAction
from src.apps.events.api.serializers import EventSerializer
from src.apps.users.api.serializers import (
    UserProfileSerializer,
    UserSerializer,
    UserUpdateProfile,
)


class UserProfileViewSet(
    SerializerPerAction, PermissionPerAction, viewsets.ModelViewSet
):
    queryset = User.objects.all()
    action_serializers = {
        "default": UserSerializer,
        "profile": UserProfileSerializer,
        "update_profile": UserUpdateProfile,
        "my_events": EventSerializer,
    }
    action_permissions = {"default": (IsAuthenticated,)}

    @action(methods=["GET"], detail=False)
    def profile(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(methods=["PATCH"], detail=False)
    def update_profile(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Профиль изменен!")

    @action(methods=["GET"], detail=False)
    def my_events(self, request: Request, *args, **kwargs):
        user = request.user
        user_events = user.events_participating.all()
        serializer = self.get_serializer(user_events, many=True)
        if user_events == []:
            return Response("Вы не участвуете в мероприятиях!")
        else:
            return Response(serializer.data)
