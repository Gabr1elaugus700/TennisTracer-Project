from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    first_name = models.CharField(max_length=50) #Todos Charfield deve passar um max_lenght
    last_name = models.CharField(max_length=50)
    old = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    login = models.CharField(max_length=50) #nome.sobrenome no cadastro
    birthday = models.DateField()
    created_in = models.DateTimeField(default=timezone.now)
    obs = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
