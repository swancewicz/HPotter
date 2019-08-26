import graphene
from graphene_django import DjangoObjectType

from .models import Connection
from .models import Credential

class ConnectionType(DjangoObjectType):
    class Meta:
        model = Connection

class CredentialType(DjangoObjectType):
    class Meta:
        model = Credential

class Query(graphene.ObjectType):
    all_connections = graphene.List(ConnectionType)
    all_credentials = graphene.List(CredentialType)

    def resolve_all_connections(self, info, **kwargs):
        return Connection.objects.all()

    def resolve_all_credentials(self, info, **kwargs):
        return Credential.objects.all()

class CreateConnection(graphene.Mutation):
    id = graphene.Int()
    country = graphene.String()
    createdAt = graphene.types.datetime.DateTime()
    sourceIP = graphene.String()
    sourcePort = graphene.Int()
    destIP = graphene.String()
    destPort = graphene.Int()
    proto = graphene.Int()
    credentials = graphene.Field(CredentialType)

    class Arguments:
        country = graphene.String()
        createdAt = graphene.types.datetime.DateTime()
        sourceIP = graphene.String()
        sourcePort = graphene.Int()
        destIP = graphene.String()
        destPort = graphene.Int()
        proto = graphene.Int()
        credentials = graphene.Int()
    
    def mutate(self, info, country, sourceIP, sourcePort, createdAt, destIP, destPort, proto, credentials):
        connection = Connection(country=country, sourceIP=sourceIP,
            sourcePort=sourcePort, createdAt=createdAt,
            destIP=destIP, destPort=destPort, proto=proto, credentials=credentials)
        
        return CreateConnection(id = country.id,
            country=connection.country,
            sourceIP = connection.sourceIP,
            createdAt=connection.createdAt,
            destIP = connection.destIP,
            destPort = connection.destPort,
            proto = connection.proto,
            credentials = credentials,
            )

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
    create_connection = CreateConnection.Field()
    create_credential = CreateCredential.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)