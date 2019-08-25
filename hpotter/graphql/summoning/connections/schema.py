import graphene
from graphene_django import DjangoObjectType

from .models import Connection
from .models import CredentialType

class ConnectionType(DjangoObjectType):
    class Meta:
        model = Connection
    
    credentials=graphene.Field(CredentialType)

class Query(graphene.ObjectType):
    allCountryAttacks = graphene.List(Connection)

    def resolve_allConnections(self, info, **kwargs):
        return Connection.objects.all()

class CreateConnection(graphene.Mutation):
    id = graphene.Int()
    country = graphene.String()
    createdAt = graphene.types.datetime.DateTime()
    sourceIP = graphene.String()
    sourcePort = graphene.Int()
    destIP = graphene.String()
    destPort = graphene.Int()
    proto = graphene.Int()

    class Arguments:
        country = graphene.String()
        createdAt = graphene.types.datetime.DateTime()
        sourceIP = graphene.String()
        sourcePort = graphene.Int()
        destIP = graphene.String()
        destPort = graphene.Int()
        proto = graphene.Int()

    
    def mutate(self, info, country, sourceIP, sourcePort, createdAt, destIP, destPort, proto):
        connection = Connection(country=country, sourceIP=sourceIP,
            sourcePort=sourcePort, createdAt=createdAt,
            destIP=destIP, destPort=destPort, proto=proto)
        
        return CreateConnection(id = country.id,
            country=connection.country,
            sourceIP = connection.sourceIP,
            createdAt=connection.createdAt,
            destIP = connection.destIP,
            destPort = connection.destPort,
            proto = connection.proto
            )

class Mutation(graphene.ObjectType):
    create_connection = CreateConnection.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)