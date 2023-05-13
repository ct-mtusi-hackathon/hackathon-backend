from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from src.apps.users.consts import UserType, UserSex
from src.apps.groups.models import Group


class User(AbstractUser):
    last_name = models.CharField(_("Фамилия"), max_length=150, blank=True)
    first_name = models.CharField(_("Имя"), max_length=150, blank=True)
    patronymic = models.CharField(_("Отчество"), max_length=150, blank=True)
    telegram_username = models.CharField(
        _("telegram username"), max_length=150, null=True
    )
    email = models.EmailField(_("Почта"), unique=True)
    phone_number = PhoneNumberField(_("Номер телефона"), region="RU", blank=True)
    sex = models.PositiveSmallIntegerField(
        choices=UserSex.choices, default=UserSex.MALE
    )
    type_account = models.PositiveSmallIntegerField(
        choices=UserType.choices, default=UserType.STUDENT
    )
    group = models.ManyToManyField(
        Group, related_name="groups", verbose_name=_("Группа пользователя")
    )

    REQUIRED_FIELDS = ["first_name", "last_name", "patronymic"]

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"
        unique_together = ("email", "type_account")
