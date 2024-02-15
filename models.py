from django.db import models

class Deporte(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)

class Instalacion(models.Model):
    id_instalacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=100)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)
    id_deporte = models.ForeignKey(Deporte, on_delete=models.RESTRICT)
    equipacion_principal = models.CharField(max_length=100)
    equipacion_suplente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.RESTRICT)
    dorsal = models.IntegerField()
    fecha_nacimiento = models.DateField()
    altura = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0)])
    peso = models.IntegerField(validators=[MinValueValidator(0)])
    telefono = models.CharField(max_length=15)

    class Meta:
        unique_together = (('id_equipo', 'dorsal'),)

class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    id_deporte = models.ForeignKey(Deporte, on_delete=models.RESTRICT)
    fecha_hora = models.DateTimeField()
    id_instalacion = models.ForeignKey(Instalacion, on_delete=models.RESTRICT, null=True, blank=True)
    id_local = models.ForeignKey(Equipo, on_delete=models.RESTRICT, related_name='local')
    id_visitante = models.ForeignKey(Equipo, on_delete=models.RESTRICT, related_name='visitante')
    puntos_local = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    puntos_visitante = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    observaciones = models.CharField(max_length=200, blank=True)
