from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "patronymic",
            "group",
            "coins",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "patronymic",
            "telegram_username",
            "email",
            "phone_number",
            "group",
            "coins",
        )


class UserUpdateProfile(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=(UniqueValidator(queryset=User.objects.all()),),
    )
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_new_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "username",
            "new_password",
            "confirm_new_password",
            "telegram_username",
        )

    def validate_old_password(self, old_password):
        user = self.context["request"].user
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {"password": "Старый пароль неверный!"},
            )

    def validate_new_password(self, new_password):
        old_password = self.initial_data.get("old_password")
        confirm_new_password = self.initial_data.get("confirm_new_password")
        if old_password == new_password:
            raise serializers.ValidationError(
                {"password": "Старый пароль совпадает с новым паролем!"},
            )

        if new_password != confirm_new_password:
            raise serializers.ValidationError(
                {"password": "Пароли не совпадают"},
            )

        return new_password

    def update(self, instance, validated_data):
        instance.email = validated_data["email"]
        instance.phone_number = validated_data["phone_number"]
        instance.username = validated_data["username"]
        instance.telegram_username = validated_data["telegram_username"]
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
