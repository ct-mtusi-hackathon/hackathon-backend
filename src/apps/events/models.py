from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.users.models.users import User
from src.apps.base.models import Image


class Event(models.Model):
    title = models.CharField(_("Название"), max_length=200)
    description = models.TextField(_("Описание"))
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(_("Место проведения"), max_length=200)
    is_active = models.BooleanField(_("Является активным"), default=True)
    coins_for_registration = models.PositiveBigIntegerField(
        _("Коины за регистрацию"), default=0
    )
    coins_for_victory = models.PositiveBigIntegerField(_("Коины за победу"), default=0)
    participants = models.ManyToManyField(
        User,
        related_name="events_participating",
        blank=True,
        verbose_name=_("Участники"),
    )

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
