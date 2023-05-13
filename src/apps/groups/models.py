from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from src.apps.groups.consts import ClassType, LetterClass


class Group(models.Model):
    class_grade = models.PositiveSmallIntegerField(
        _("Класс"), choices=ClassType.choices, default=ClassType.NINTH_GRADE
    )
    number_course = models.PositiveSmallIntegerField(_("Номер курса"), default=1)
    date_of_creation = models.DateField(_("Дата создания"), default=timezone.now)
    letter_group = models.CharField(
        _("Буква группы"), choices=LetterClass.choices, default=LetterClass.AP
    )
    direction = models.ForeignKey(
        "Direction",
        on_delete=models.CASCADE,
        related_name="groups",
        verbose_name=_("Направление"),
    )

    def __str__(self) -> str:
        return (
            f"{self.direction.short_name}"
            f"{self.class_grade}-{self.number_course}"
            f"{str(self.date_of_creation.year)[2:]}{self.letter_group}"
        )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["number_course"]


class Direction(models.Model):
    name = models.CharField(_("Название направления"), max_length=150)
    short_name = models.CharField(_("Сокращенное название"), max_length=20)
    code = models.CharField(_("Код напраления"), max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Направление колледжа"
        verbose_name_plural = "Направления колледжа"
        unique_together = ("name", "short_name", "code")
