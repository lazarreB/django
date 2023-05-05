from django.db import models
from datetime import datetime

# Create your models here.
class Machine(models.Model):
    TYPE = (
        ('PC',('PC - run windows')),
        ('Mac',('Mac - run MacOS')),
        ('Server',('Server - Simple Server to deply virtual machine')),
        ('Switch',('Switch - To maintains  and connect servers' )),
    )
    id = models.AutoField(primary_key=True,editable=False)
    nom = models.CharField(max_length= 6)
    maintenaceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')

class Personne(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    nom = models.CharField(
        max_length= 6)
    
    def __str__(self):
        
        return str(self.id) + " -> " + self.nom

    def get_name(self):

        return str(self.id) + " " + self.nom