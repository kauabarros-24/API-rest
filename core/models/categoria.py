from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    #Adiciconado por Kaua
    nome = models.CharField(max_length=50, default="Sem nome")
    idade = models.IntegerField(default=10)
    autor = models.CharField(max_length=100)
    #Não usar return self.x, self.y
    def __str__(self):
        return self.descricao
        return self.nome
        return self.autor
    



