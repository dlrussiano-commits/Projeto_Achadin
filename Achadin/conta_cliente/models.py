from django.db import models

# Importei uma classe específica para avitar desenvolver uma lógica para a autenticação

from django.contrib.auth.models import User

# Importei uma biblioteca específica pra fazer a validação do número de telefone

from phonenumber_field.modelfields import PhoneNumberField

# Importei uma classe específica pra fazer a validação do CPF

from rest_framework.exceptions import ValidationError

# Create your models here.

# Como o Django não tem um campo pronto de CPF, é necessário fazer uma validação

def validacao_cpf(cpf):
    if len(cpf) != 11:
        raise ValidationError("O CPF deve conter 11 dígitos")


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Nome do usuário (geralmente tem 30 caracteres)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telefone = PhoneNumberField(region="BR", unique=True)
    cpf = models.CharField(unique=True, validators=[validacao_cpf])
    endereco = models.CharField(max_length=100)

