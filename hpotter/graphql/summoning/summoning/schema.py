import graphene

from graphene_django.types import DjangoObjectType
import credentials.schema
import connections.schema

#class PasswordType(DjangoObjectType):
    #model = Password

class Query(credentials.schema.Query, graphene.ObjectType):
    pass

class Mutation(credentials.schema.Mutation, graphene.ObjectType):
    pass

class Query(connections.schema.Query, graphene.ObjectType):
    pass

class Mutation(connections.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

val = '''
    all_passwords = graphene.List(PasswordType)

    def resolve_all_passwords(self, info, **kwargs):
        return Password.objects.all()
        '''