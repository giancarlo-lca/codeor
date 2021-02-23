from django.db import models
from django.contrib.auth.models import User

from apps.pi.models import Pi

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=100)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pi = models.ForeignKey(Pi, on_delete=models.SET_NULL, null=True ,blank=True)


    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'funcionarios'
