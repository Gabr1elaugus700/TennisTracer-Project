from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Aula(models.Model):
    day = models.CharField(max_length=50)
    hora_ini = models.TimeField()
    hora_fim = models.TimeField()
    
    def __str__(self) -> str:
        return f'{self.id} {self.day} {self.hora_ini}'

class Aluno(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    old = models.IntegerField()  # Usar IntegerField para idade
    phone = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    birthday = models.DateField()
    created_in = models.DateTimeField(default=timezone.now)
    obs = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    category = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name}'

class Aluno_Aula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True)  # Corrigido para permitir NULL
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)  # Corrigido para permitir NULL

    def __str__(self) -> str:
        return f'{self.id} {self.aula} {self.aluno}'
