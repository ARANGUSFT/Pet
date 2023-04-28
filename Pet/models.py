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