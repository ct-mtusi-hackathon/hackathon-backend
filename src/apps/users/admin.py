from django.contrib import admin

from src.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
