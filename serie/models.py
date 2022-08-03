from django.db import models

# Create your models here.
class Serie(models.Model):
    nome = models.CharField(max_length=80)
    sinopse = models.CharField(max_length=300)
    num_episodios = models.IntegerField()
    data_lancamento = models.DateField()