from graphql_jwt.decorators import user_passes_test
from .models import User

is_owner = user_passes_test(
    lambda user: user.is_authenticated and (user.type == User.Types.ADMIN or user.type == User.Types.OWNER))

is_admin = user_passes_test(lambda user: user.is_authenticated and (user.type == User.Types.ADMIN))

is_client = user_passes_test(
    lambda user: user.is_authenticated and (user.type == User.Types.ADMIN or user.type == User.Types.CLIENT))
