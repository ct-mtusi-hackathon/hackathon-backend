from datetime import datetime as dt

from django.db import models
from django.utils.translation import gettext_lazy as _


DEFAULT_YEAR = dt.now().year


class ClassType(models.IntegerChoices):
    NINTH_GRADE = 9, "9 класс"
    ELEVENTH_GRADE = 11, "11 класс"


class LetterClass(models.TextChoices):
    AP = (
        "АП",
        _("АП"),
    )
    BP = (
        "БП",
        _("БП"),
    )
    VP = (
        "ВП",
        _("ВП"),
    )
    P = "П", _("П")
