from django.db import models

# Create your models here.

# un título, descripción, fecha de vencimiento y categoría.

class CategoriaTarea(models.Model):
    nameCat = models.CharField(max_length=50)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nameCat)

class Tarea(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    dt_vencimiento = models.DateField()
    categoria = models.ForeignKey(CategoriaTarea, on_delete=models.CASCADE)
    realizada = models.BooleanField(default=False)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.titulo)