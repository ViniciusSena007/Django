from django.db import models

# Create your models here.
class Cursos(models.Model):
    curso = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.curso