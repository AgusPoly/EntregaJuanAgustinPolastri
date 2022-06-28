from django.contrib import admin
from App import models  #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(models.Curso)

admin.site.register(models.Estudiante)

admin.site.register(models.Profesor)

admin.site.register(models.Entregable)
