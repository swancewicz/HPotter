import graphene

from graphene_django.types import DjangoObjectType
import connections.schema

#class PasswordType(DjangoObjectType):
    #model = Password
class Query(connections.schema.Query, graphene.ObjectType):
    pass

class Mutation(connections.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)