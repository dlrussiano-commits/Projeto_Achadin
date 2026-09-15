from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from conta_cliente.models import validacao_cpf


# Create your models here.

def validacao_cnpj(cnpj):
    if len(cnpj) != 14:
        raise ValidationError("Seu CNPJ deve conter 14 números")

class Logista(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    cpf = models.CharField(unique=True, validators=[validacao_cpf])
    cnae = models.CharField(unique=True)
    cnpj = models.CharField(unique=True, validators=[validacao_cnpj])
    telefone = PhoneNumberField(unique=True, region='BR')

