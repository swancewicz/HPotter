from django.db import models

# Create your models here.
class Credential(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Connection(models.Model):
    country = models.CharField(max_length=100)
    createdAt = models.DateField()
    sourceIP = models.CharField(max_length=20)
    sourcePort = models.CharField(max_length=10)
    destIP = models.CharField(max_length=50)
    destPort = models.IntegerField()
    proto = models.IntegerField()
    credentials = models.ForeignKey(Credential, 
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.country

class HttpCommands(models.Model):
    request = models.CharField(max_length=10000)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)

    def __str__(self):
        return self.request

class ShellCommands(models.Model):
    command = models.CharField(max_length=100)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)

    def __str__(self):
        return self.command

class SqlCommands(models.Model):
    request = models.CharField(max_length=10000)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)

    def __str__(self):
        return self.request