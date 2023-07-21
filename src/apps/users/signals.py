from src.apps.users.models.accounts import UserAccount


def create_user_account(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)
