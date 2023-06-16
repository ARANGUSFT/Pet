from django.db import models
from django.contrib.auth.models import User



class Mascota(models.Model):
    Id_Mascota = models.AutoField(primary_key=True)
    Nombre_M = models.TextField(max_length=50)
    Raza_M = models.TextField(max_length=50)
    Color_M = models.TextField(max_length=50)
    Foto_M = models.ImageField(upload_to="ImagenesBD/", null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
      db_table = 'tbl_mascota'


class Dueno(models.Model):
    Id_Dueno = models.AutoField(primary_key=True)
    Nombre_Completo_D = models.TextField(max_length=150)
    Celular_D = models.TextField(max_length=20)
    Celular_Secundario_D = models.TextField(max_length=20)
    Correo_D = models.TextField(max_length=150)
    Municipio_D = models.TextField(max_length=50) 
    Mascota_Id = models.ForeignKey(Mascota, on_delete=models.CASCADE, db_column='Mascota_Id')
    codigo_qr_url = models.URLField(null=True, blank=True)
    codigo_qr_nombre_archivo = models.ImageField(max_length=255, null=True, blank=True)

    class Meta:
      db_table = 'tbl_Dueno'


class Caracteristicas(models.Model):
    Id_Caracteristicas = models.AutoField(primary_key=True)
    Estilo_Placa_C = models.TextField(max_length=50)
    Estilo_Color_C = models.TextField(max_length=50)
    Dueno_Id = models.ForeignKey(Dueno, on_delete=models.CASCADE, db_column='Dueno_Id')

    class Meta:
      db_table = 'tbl_Caracteristicas'


class Envio(models.Model):
    Id_Envio = models.AutoField(primary_key=True)
    Direccion = models.TextField(max_length=256)
    Barrio = models.TextField(max_length=256)
    Detalles = models.TextField(max_length=256)
    Dueno_Id = models.ForeignKey(Dueno, on_delete=models.CASCADE, db_column='Dueno_Id')

    class Meta:
      db_table = 'tbl_Envio'









