from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator


def index(request):
    title = 'Aulas'

    aulas = Aula.objects.filter(coach=1) 

    paginator = Paginator(aulas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    alunos_aula = Aluno_Aula.objects.all()
    context = {
        'title': title,
        'alunos_aula': alunos_aula,
        'page_obj': page_obj
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