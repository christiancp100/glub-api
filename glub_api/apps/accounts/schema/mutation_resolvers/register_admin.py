import graphene
from accounts.schema import CustomUserNode
from accounts.models import User, AdminInfo
from accounts import is_admin


# noinspection DuplicatedCode
class RegisterAdminMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        role = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(CustomUserNode)

    @classmethod
    @is_admin
    def mutate(cls, root, info, username, password, email, role, first_name, last_name):
        user = User.objects.create_user(email=email, username=username, password=password)
        user.type = User.Types.ADMIN
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        admin_info = AdminInfo.objects.create(user=user)
        admin_info.role = role
        admin_info.save()

        return RegisterAdminMutation(user=user)
