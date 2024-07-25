from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'picture',
    ordering = 'id',

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = 'id', 'day', 'hora_ini', 'hora_fim',
    ordering = '-id',

@admin.register(models.Aluno_Aula)
class Aluno_AulaAdmin(admin.ModelAdmin):
    list_display = 'id', 'aula', 'aluno',
    ordering = 'id',