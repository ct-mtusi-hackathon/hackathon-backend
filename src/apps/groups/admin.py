from django.contrib import admin

from src.apps.groups.models import Group, Direction


@admin.register(Direction)
class OrientationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        "code",
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
