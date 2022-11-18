from django.db import models
from django.utils import timezone


class TypeDemande(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Service(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Ordinateur(models.Model):
    reference = models.CharField(max_length=100)

    def __str__(self):
        return self.reference


class OrdinateurData(models.Model):
    pcbrand = models.CharField(max_length=100, default="")
    cpu = models.CharField(max_length=100, default="")
    disc = models.CharField(max_length=100, default="")
    ram = models.CharField(max_length=100, default="")
    graphicCard = models.CharField(max_length=100, default="")




class Telephone(models.Model):
    reference = models.CharField(max_length=100)

    def __str__(self):
        return self.reference


class TelephoneData(models.Model):
    phonebrand = models.CharField(max_length=100, default="")
    conf = models.CharField(max_length=100, default="")
    operateur = models.CharField(max_length=100, default="")
    internet = models.CharField(max_length=100, default="")
    appel = models.CharField(max_length=100, default="")


class Acces(models.Model):
    reference = models.CharField(max_length=100)

    def __str__(self):
        return self.reference

class AccesData(models.Model):
    internet = models.CharField(max_length=100, default="")
    restreint = models.CharField(max_length=100, default="")
    network = models.CharField(max_length=100, default="")
    programs = models.CharField(max_length=100, default="")


class Employee(models.Model):
    reference = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50, default=None)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, blank=True, null=True)
    password = models.CharField(max_length=100)
    dateStart = models.DateTimeField(default=timezone.now)
    workplace = models.CharField(max_length=50, default=None)
    job = models.CharField(max_length=50, default=None)
    refAcces = models.CharField(max_length=50, null=True, blank=True)
    refOrdi = models.CharField(max_length=50, null=True, blank=True)
    refPhone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    typeDemande = models.ForeignKey(TypeDemande, on_delete=models.PROTECT)
    ordinateur  = models.CharField(max_length=100, blank=True, null=True)
    telephone  = models.CharField(max_length=100, blank=True, null=True)
    acces  = models.CharField(max_length=100, blank=True, null=True)
    description  = models.TextField(blank=True, null=True)
    employe = models.ForeignKey(Employee, on_delete=models.PROTECT)
    sendBy = models.CharField(max_length=100)
    receiver = models.ForeignKey(Service, on_delete=models.PROTECT)
    dateReceiver = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)
    file  = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __int__(self):
        return self.id


