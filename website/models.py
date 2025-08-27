from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Contexto(models.Model):
    info_geral = models.TextField()

    def __str__(self):
        return self.info_geral[:50]  # Retorna os primeiros 50 caracteres da descrição
    
class Elenco(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    imagem = models.ImageField(upload_to='website/media/')
    personagem = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=100)   

    def __str__(self):
        return self.nome
    
class Info_Site(models.Model):
    descricao = models.TextField()
    autores = models.TextField(help_text="Liste os autores separados por vírgulas")

    def get_autores_list(self):
        return [autor.strip() for autor in self.autores.split(',')]

    def __str__(self):
        return self.descricao[:50]  # Retorna os primeiros 50 caracteres da descrição