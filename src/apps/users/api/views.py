from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from src.apps.users.models import User
from src.apps.base.api.mixins import PermissionPerAction, SerializerPerAction
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
    }
    action_permissions = {"default": (IsAuthenticated,)}

    @action(methods=["GET"], detail=True)
    def profile(self, request: Request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    @action(methods=["PATCH"], detail=True)
    def update_profile(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Профиль изменен!")
