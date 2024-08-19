from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    title = 'Aulas'

    # Obter as aulas do coach específico
    aulas = Aula.objects.filter(coach=1)
    alunos = alunos = Aluno.objects.all()

    # Paginar as aulas
    paginator = Paginator(aulas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Contexto atualizado para passar os alunos relacionados a cada aula
    context = {
        'title': title,
        'page_obj': page_obj,
        'alunos': alunos,
        'MEDIA_URL': settings.MEDIA_URL
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
        'tennisTracer/profileCoach.html',
        context,
    )

# def profile(request):
#     title = 'Perfil'
#     aluno = get_object_or_404(Aluno, pk=contact_id)
#     # aluno = Aluno.objects.get(pk=contact_id)
#     context = {
#         'title': title,
#         'aluno': aluno
#     }

#     return render(
#         request, 
#         'tennisTracer/createdAluno.html',
#         context,
#     )

def profileCoach(request):
    title = 'Perfil'
    # aluno = get_object_or_404(Aluno, pk=contact_id)
    # aluno = Aluno.objects.get(pk=contact_id)
    context = {
        'title': title,
    }

    return render(
        request, 
        'tennisTracer/profileCoach.html',
        context,
    )