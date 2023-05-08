from rest_framework import serializers

from src.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "phone_number",
            "telegram_username",
            "type_account",
        )
