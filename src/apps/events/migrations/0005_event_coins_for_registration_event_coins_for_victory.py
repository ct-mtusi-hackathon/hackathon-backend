# Generated by Django 4.2.1 on 2023-05-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_event_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="coins_for_registration",
            field=models.PositiveBigIntegerField(
                default=0, verbose_name="Коины за регистрацию"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="coins_for_victory",
            field=models.PositiveBigIntegerField(
                default=0, verbose_name="Коины за победу"
            ),
        ),
    ]
