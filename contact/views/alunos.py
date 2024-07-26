from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect


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

def profile(request, contact_id):
    title = 'Perfil'
    aluno = get_object_or_404(Aluno, pk=contact_id)
    # aluno = Aluno.objects.get(pk=contact_id)
    context = {
        'title': title,
        'aluno': aluno
    }

    return render(
        request, 
        'tennisTracer/createdAluno.html',
        context,
    )