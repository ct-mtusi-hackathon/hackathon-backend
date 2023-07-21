from django.contrib import admin

from src.apps.users.models.users import User
from src.apps.users.models.accounts import UserAccount


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass
