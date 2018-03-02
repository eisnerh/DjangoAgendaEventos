from django.db import models
from django.utils import timezone


# Create your models here.

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    Nombre_cliente = models.CharField(max_length=45)
    Apellido_cliente = models.CharField(max_length=45)
    Telefono_cliente = models.CharField(max_length=45)
    Correo_electronico = models.CharField(max_length=45)
    Otros_datos_cliente = models.TextField()


class ClasificacionEvento(models.Model):
    idClasificacion_evento = models.AutoField(primary_key=True)
    Clasificacion_evento = models.CharField(max_length=45)

    def __str__(self):
        return '<Clasificacion: {}>'.format(self.Clasificacion_evento)


class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    NombreEvento = models.CharField(max_length=45)
    CodigoEvento = models.CharField(max_length=45)

    def __str__(self):
        return '<Nombre Evento: {}, Codigo Evento: {}>'.format(self.NombreEvento, self.CodigoEvento)


class DetalleEvento(models.Model):
    idDetalle_evento = models.AutoField(primary_key=True)
    FechaInicio = models.DateField(default=timezone.now)
    FechaFin = models.DateField()
    ClasificacionEvento_idClasificacionEvento = models.ForeignKey(ClasificacionEvento, on_delete=models.CASCADE)
    Evento_idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class EventoCliente(models.Model):
    idEventoCliente = models.AutoField(primary_key=True)
    ClienteIdCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    EventoIdEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True)
    CodigoMaterial = models.CharField(max_length=45)
    nombreMaterial = models.CharField(max_length=45)
    CantidadIdeal = models.IntegerField()
    CantidadInicial = models.IntegerField()

    def __str__(self):
        return '<Codigo Material: {}, Nombre Materia: {}>'.format(self.CodigoMaterial, self.nombreMaterial)


class EventoMaterial(models.Model):
    idEventoMaterial = models.AutoField(primary_key=True)
    EventoIdEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    MaterialIdMaterial = models.ForeignKey(Material, on_delete=models.CASCADE)