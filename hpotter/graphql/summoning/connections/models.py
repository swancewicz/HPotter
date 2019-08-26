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