import graphene
from graphene_django import DjangoObjectType
from geolite2 import geolite2

from .models import Connection
from .models import Credential
from .models import HttpCommands
from .models import ShellCommands
from .models import SqlCommands

class ConnectionType(DjangoObjectType):
    class Meta:
        model = Connection

class CredentialType(DjangoObjectType):
    class Meta:
        model = Credential

class HttpCommandsType(DjangoObjectType):
    class Meta:
        model = HttpCommands

class ShellCommandsType(DjangoObjectType):
    class Meta:
        model = ShellCommands

class SqlCommandsType(DjangoObjectType):
    class Meta:
        model = SqlCommands

class Query(graphene.ObjectType):
    all_connections = graphene.List(ConnectionType)
    all_credentials = graphene.List(CredentialType)
    all_http_commands = graphene.List(HttpCommandsType)
    all_shell_commands = graphene.List(ShellCommandsType)
    all_sql_commands = graphene.List(SqlCommandsType)

    def resolve_all_connections(self, info, **kwargs):
        return Connection.objects.all()

    def resolve_all_credentials(self, info, **kwargs):
        return Credential.objects.all()
    
    def resolve_all_http_commands(self, info, **kwargs):
        return HttpCommand.objects.all()
    
    def resolve_all_shell_commands(self, info, **kwargs):
        return ShellCommand.objects.all()
    
    def resolve_all_sql_commands(self, info, **kwargs):
        return SqlCommand.objects.all()

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
        #country = graphene.String()
        createdAt = graphene.types.datetime.DateTime()
        sourceIP = graphene.String()
        sourcePort = graphene.Int()
        destIP = graphene.String()
        destPort = graphene.Int()
        proto = graphene.Int()
        credentials = graphene.Int()
    
    def mutate(self, info, sourceIP, sourcePort, createdAt, destIP, destPort, proto, credentials):
        reader = geolite2.reader() #TODO move this somewhere else
        info = reader.get(sourceIP)
        if "country" in info.keys():
            country = info['country']['names']['en']
        else:
            country = None
        credentials = Credential.objects.filter(id=credentials).first()
        connection = Connection(country=country, sourceIP=sourceIP,
            sourcePort=sourcePort, createdAt=createdAt,
            destIP=destIP, destPort=destPort, proto=proto, credentials=credentials)
        connection.save(connection)

        return CreateConnection(
            id = connection.id,
            country=connection.country,
            sourceIP = connection.sourceIP,
            createdAt=connection.createdAt,
            sourcePort=connection.sourcePort,
            destIP = connection.destIP,
            destPort = connection.destPort,
            proto = connection.proto,
            credentials = connection.credentials,
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
        Credential.save(credential)

        return CreateCredential(id = credential.id,
                                username=credential.username,
                                password = credential.password)

class CreateHttpCommand(graphene.Mutation):
    id = graphene.Int()
    request = graphene.String()
    connection = graphene.Field(ConnectionType)

    class Arguments:
        request = graphene.String()
        connection = graphene.Int()
    
    def mutate(self, info, request, connection):
        connection = Connection.objects.filter(id=connection).first()
        #TODO need error message here if not in db
        httpCommand = HttpCommands(request=request, connection=connection)
        HttpCommands.save(httpCommand)

        return CreateHttpCommand(id = httpCommand.id,
                                request=httpCommand.request,
                                connection = httpCommand.connection)

class CreateShellCommand(graphene.Mutation):
    id = graphene.Int()
    command = graphene.String()
    connection = graphene.Field(ConnectionType)

    class Arguments:
        command = graphene.String()
        connection = graphene.Int()
    
    def mutate(self, info, command, connection):
        connection = Connection.objects.filter(id=connection).first()
        #TODO need error message here
        shellCommand = ShellCommands(command=command, connection=connection)
        ShellCommands.save(shellCommand)

        return CreateShellCommand(id = shellCommand.id,
                                command=shellCommand.command,
                                connection = shellCommand.connection)

class CreateSqlCommand(graphene.Mutation):
    id = graphene.Int()
    request = graphene.String()
    connection = graphene.Field(ConnectionType)

    class Arguments:
        command = graphene.String()
        connection = graphene.Int()
    
    def mutate(self, info, request, connection):
        connection = Connection.objects.filter(id=connection).first()
        #TODO need error message here
        sqlCommand = ShellCommands(request=request, connection=connection)
        SqlCommands.save(sqlCommand)

        return CreateSqlCommand(id = sqlCommand.id,
                                command=sqlCommand.request,
                                connection = sqlCommand.connection)

class Mutation(graphene.ObjectType):
    create_connection = CreateConnection.Field()
    create_credential = CreateCredential.Field()
    create_http_command = CreateHttpCommand.Field()
    create_shell_command = CreateShellCommand.Field()
    create_sql_command = CreateSqlCommand.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)