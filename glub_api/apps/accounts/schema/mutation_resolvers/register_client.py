import graphene
from accounts.schema import CustomUserNode
from accounts.models import User, ClientInfo


class RegisterClientMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        birthday = graphene.DateTime(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(CustomUserNode)

    @classmethod
    def mutate(cls, root, info, username, password, email, birthday, first_name, last_name):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.type = User.Types.CLIENT
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        owner_info = ClientInfo.objects.create(user=user, birthday=birthday)
        owner_info.save()

        return RegisterClientMutation(user=user)
