import graphene
from accounts.schema import CustomUserNode
from accounts.models import User
from accounts import is_admin


class UserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=False)

    user = graphene.Field(CustomUserNode)

    @classmethod
    @is_admin
    def mutate(cls, root, info, username, email=None):
        user = User.objects.get(username=username)
        if email is not None:
            user.email = email
        user.save()
        return UserMutation(user=user)
