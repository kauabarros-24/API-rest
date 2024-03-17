from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    editora = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo, self.categoria, self.editora