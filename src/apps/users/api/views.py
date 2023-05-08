from rest_framework import viewsets

from src.apps.users.models import User
from src.apps.users.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
