from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    telefone = models.CharField(max_length=18, default=None)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome