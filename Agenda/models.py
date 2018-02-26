

from django.db import models


# Create your models here.

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    Nombre_cliente = models.TextField()
    Apellido_cliente = models.TextField()
    Telefono_cliente = models.TextField()
    Correo_electronico = models.TextField()
    Otros_datos_cliente = models.TextField()


class ClasificacionEvento(models.Model):
    idClasificacion_evento = models.AutoField(primary_key=True)
    Clasificacion_evento = models.TextField()


class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    NombreEvento = models.TextField()
    CodigoEvento = models.TextField()


class DetalleEvento(models.Model):
    idDetalle_evento = models.AutoField(primary_key=True)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    ClasificacionEvento_idClasificacionEvento = models.ForeignKey(ClasificacionEvento, on_delete=models.CASCADE)
    Evento_idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class EventoCliente(models.Model):
    idEventoCliente = models.AutoField(primary_key=True)
    ClienteIdCliente = models.IntegerField()
    EventoIdEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True)
    CodigoMaterial = models.TextField()
    nombreMaterial = models.TextField()
    CantidadIdeal = models.IntegerField()
    CantidadInicial = models.IntegerField()


class EventoMaterial(models.Model):
    idEventoMaterial = models.AutoField(primary_key=True)
    EventoIdEvento = models.IntegerField()
    MaterialIdMaterial = models.ForeignKey(Material, on_delete=models.CASCADE)