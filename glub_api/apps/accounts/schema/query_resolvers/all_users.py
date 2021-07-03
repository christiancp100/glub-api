from accounts.models import User


def resolve_all_users():
    return User.objects.all()
