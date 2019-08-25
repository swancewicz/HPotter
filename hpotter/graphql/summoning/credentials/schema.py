import graphene
from graphene_django import DjangoObjectType

from .models import Credential

class CredentialType(DjangoObjectType):
    class Meta:
        model = Credential

class Query(graphene.ObjectType):
    all_credentials = graphene.List(CredentialType)

    def resolve_all_credentials(self, info, **kwargs):
        return Credential.objects.all()

class CreateCredential(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    password = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()
    
    def mutate(self, info, username, password):
        credential = Credential(username=username, password=password)
        credential.save()

        return CreateCredential(id = credential.id,
                                username=credential.username,
                                count = credential.password)

class Mutation(graphene.ObjectType):
    create_credential = CreateCredential.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)