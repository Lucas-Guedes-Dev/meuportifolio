from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome