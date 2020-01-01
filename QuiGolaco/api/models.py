from django.db import models


class Jogadores(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    altura = models.CharField(max_length=5)
    num_gols = models.IntegerField()
    num_assistencias = models.IntegerField()

    def __str__(self):
        return "Nome: " + self.nome + " | Núm de Gols: " + str(self.num_gols) + " | Núm de Assistências: " + str(self.num_assistencias)

    class Meta:
        verbose_name_plural = "Jogadores"
