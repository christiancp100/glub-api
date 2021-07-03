from graphene import relay
from graphene_django import DjangoObjectType
from accounts.models import User, ClientInfo, AdminInfo, OwnerInfo


class CustomUserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username']
        exclude = ('password',)
        interfaces = (relay.Node,)


class ClientInfoNode(DjangoObjectType):
    class Meta:
        model = ClientInfo


class AdminInfoNode(DjangoObjectType):
    class Meta:
        model = AdminInfo


class OwnerInfoNode(DjangoObjectType):
    class Meta:
        model = OwnerInfo

