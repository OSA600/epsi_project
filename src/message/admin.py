from django.contrib import admin
from .models import Message, TypeDemande, Service, Employee, Ordinateur, Telephone, Acces, AccesData, TelephoneData, \
    OrdinateurData

# Register your models here.


# Register your models here.
admin.site.register(Message)
admin.site.register(TypeDemande)
admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(Ordinateur)
admin.site.register(Telephone)
admin.site.register(Acces)
admin.site.register(AccesData)
admin.site.register(TelephoneData)
admin.site.register(OrdinateurData)