from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    ...