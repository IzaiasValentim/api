from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    nome_completo = models.CharField(
        max_length=50, null=False, blank=False)

    cpf = models.CharField(
        unique=True, max_length=14, null=False, blank=False)

    email = models.EmailField(
        unique=True, max_length=50, null=False, blank=False)

    telefone = models.CharField(max_length=14, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    data_criacao = models.DateField(auto_now_add=True, editable=False)
    data_atualizacao = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
