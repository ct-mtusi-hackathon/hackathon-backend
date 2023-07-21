import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class UserAccount(models.Model):
    account_number = models.UUIDField(
        _("Номер счета"),
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    coins = models.PositiveIntegerField(_("Количество коинов"), default=0)
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="coins"
    )

    def __str__(self) -> str:
        return f"{self.account_number}"

    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"
