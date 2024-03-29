# Generated by Django 4.2.3 on 2023-07-21 09:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Direction",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Название направления"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        max_length=20, verbose_name="Сокращенное название"
                    ),
                ),
                (
                    "code",
                    models.CharField(max_length=50, verbose_name="Код напраления"),
                ),
            ],
            options={
                "verbose_name": "Направление колледжа",
                "verbose_name_plural": "Направления колледжа",
                "unique_together": {("name", "short_name", "code")},
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                (
                    "class_grade",
                    models.PositiveSmallIntegerField(
                        choices=[(9, "9 класс"), (11, "11 класс")],
                        default=9,
                        verbose_name="Класс",
                    ),
                ),
                (
                    "number_course",
                    models.PositiveSmallIntegerField(
                        default=1, verbose_name="Номер курса"
                    ),
                ),
                (
                    "date_of_creation",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Дата создания"
                    ),
                ),
                (
                    "letter_group",
                    models.CharField(
                        choices=[("АП", "АП"), ("БП", "БП"), ("ВП", "ВП"), ("П", "П")],
                        default="АП",
                        verbose_name="Буква группы",
                    ),
                ),
                (
                    "direction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="groups.direction",
                        verbose_name="Направление",
                    ),
                ),
            ],
            options={
                "verbose_name": "Группа",
                "verbose_name_plural": "Группы",
                "ordering": ["number_course"],
            },
        ),
    ]
