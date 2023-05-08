from django.db import models
from django.utils.translation import gettext_lazy as _


class UserType(models.IntegerChoices):
    STUDENT = 1, _("Студент")
    TUTOR = 2, _("Куратор")
