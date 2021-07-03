import graphene
from .mutation_resolvers.update_user import UserMutation
from .mutation_resolvers import RegisterOwnerMutation, RegisterClientMutation, RegisterAdminMutation


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()
    register_owner = RegisterOwnerMutation.Field()
    register_admin = RegisterAdminMutation.Field()
    register_client = RegisterClientMutation.Field()
