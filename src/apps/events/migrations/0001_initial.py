# Generated by Django 4.2.3 on 2023-07-21 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "location",
                    models.CharField(max_length=200, verbose_name="Место проведения"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Является активным"),
                ),
                (
                    "coins_for_registration",
                    models.PositiveBigIntegerField(
                        default=0, verbose_name="Коины за регистрацию"
                    ),
                ),
                (
                    "coins_for_victory",
                    models.PositiveBigIntegerField(
                        default=0, verbose_name="Коины за победу"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.image",
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="events_participating",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Участники",
                    ),
                ),
            ],
            options={
                "verbose_name": "Мероприятие",
                "verbose_name_plural": "Мероприятия",
            },
        ),
    ]
