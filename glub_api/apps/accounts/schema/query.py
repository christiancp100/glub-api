import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from accounts.models import User
from accounts import is_admin

from .nodes import CustomUserNode
from .query_resolvers import resolve_all_users


class Query(graphene.ObjectType):
    all_users = DjangoFilterConnectionField(CustomUserNode)

    user_by_username = relay.Node.Field(CustomUserNode, username=graphene.String(required=True))

    @is_admin
    def resolve_all_users(root, info, **kwargs):
        resolve_all_users()

    def resolve_user_by_username(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
