from django.db import models

# Create your models here.
class Carteira(models.Model):
    id_carteira = models.AutoField(primary_key=True)
    valor = models.FloatField()

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    nome = models.TextField()
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    email = models.TextField()
    data_nascimento = models.DateField()

class Odds(models.Model):
    id_odds = models.AutoField(primary_key=True)
    odd_casa = models.FloatField()
    odd_empate = models.FloatField()
    odd_fora = models.FloatField()

class Campeonatos(models.Model):
    id_campeonato = models.AutoField(primary_key=True)
    nome = models.TextField()

class Partidas(models.Model):
    id_partida = models.AutoField(primary_key=True)
    id_campeonato = models.ForeignKey(Campeonatos, on_delete=models.CASCADE)
    id_odds = models.ForeignKey(Odds, on_delete=models.CASCADE)
    time_casa = models.TextField()
    time_fora = models.TextField()
    horario = models.DateTimeField()

class TipoAposta(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome = models.TextField()

class Apostas(models.Model):
    id_aposta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)
    id_partida = models.ForeignKey(Partidas, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(TipoAposta, on_delete=models.CASCADE)
    valor = models.FloatField()
    retorno = models.FloatField()
    resultado = models.IntegerField(null=True, blank=True)
    finalizada = models.IntegerField(null=True, blank=True)


