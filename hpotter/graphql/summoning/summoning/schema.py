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

val = '''
    all_passwords = graphene.List(PasswordType)

    def resolve_all_passwords(self, info, **kwargs):
        return Password.objects.all()
        '''