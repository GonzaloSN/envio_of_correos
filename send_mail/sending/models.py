from django.db import models
from django.db.models.fields import EmailField
# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class RegionalUser(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=30)
    last_name = models.CharField(verbose_name='Apellido', max_length=30)
    email = models.EmailField(verbose_name='E-mail', max_length=30)
    username = models.CharField(verbose_name='Nombre de Usuario', max_length=60)
    password = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Perfil')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Región')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    

