from contact.models import *
from django.shortcuts import get_object_or_404, render


def index(request):
    title = 'Aulas'
    alunos_aula = Aluno_Aula.objects.all()
    context = {
        'title': title,
        'alunos_aula': alunos_aula
    }

    return render(
        request, 
        'tennisTracer/day.html',
        context,
    )