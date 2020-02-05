from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Semoviente(models.Model):
    chapeta = models.CharField(max_length=40)
    fecha_ingreso = models.CharField(max_length=40)

    def __str__(self):
        return self.chapeta + " " + self.fecha_ingreso