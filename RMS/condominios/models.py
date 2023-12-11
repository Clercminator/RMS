from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.

class Condominio(models.Model):

    TYPES = (
                ('Edificio','Edificio'),
                ('Casa','Casa'),
            )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #CASCADE means that whenever an user is deleted, the relationship to that customer will be deleted as well. A OneToOne field means that an user can have one customer and a customer can only have one user.
    name = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True, choices=TYPES)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Banco(models.Model):

    condominio = models.ForeignKey(Condominio, null=True, on_delete= models.SET_NULL)
    bank_name = models.CharField(max_length=200, null=True)
    bank_account = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.condominio.name
    

class Gasto(models.Model):

    condominio = models.ForeignKey(Condominio, null=True, on_delete= models.SET_NULL)
    gasto = models.CharField(max_length=200, null=True)
    monto = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    note = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.condominio.name