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


    class Meta:
      db_table = 'tbl_Dueno'

class Caracteristicas(models.Model):
    Id_Caracteristicas = models.AutoField(primary_key=True)
    Estilo_Placa_C = models.TextField(max_length=50)
    Color_Placa_C = models.TextField(max_length=50)
    Dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)

    class Meta:
      db_table = 'tbl_Caracteristicas'








