import graphene
from accounts.schema import CustomUserNode
from accounts.models import User, OwnerInfo
from accounts import is_admin


class RegisterOwnerMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        nif = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(CustomUserNode)

    @classmethod
    @is_admin
    def mutate(cls, root, info, username, password, email, nif, first_name, last_name):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.type = User.Types.OWNER
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        owner_info = OwnerInfo.objects.create(user=user)
        owner_info.nif = nif
        owner_info.save()

        return RegisterOwnerMutation(user=user)
