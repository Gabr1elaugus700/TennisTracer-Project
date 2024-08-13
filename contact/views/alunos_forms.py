from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from contact.forms import CreateTemaAula, CreateAluno


def createTemaAula(request):
    if request.method == 'POST':

        title = 'Cadastrar Nova Aula'

        context = {
            'title': title,
            'form': CreateTemaAula(request.POST)
        }

        return render(
            request, 
            'tennisTracer/createTemaAula.html',
            context,
        )

    title = 'Cadastrar Nova Aula'

    context = {
        'title': title,
        'form': CreateTemaAula
    }

    return render(
        request, 
        'tennisTracer/createTemaAula.html',
        context,
    )

def createAluno(request):
    if request.method == 'POST':

        title = 'Cadastrar Novo Aluno'

        context = {
            'title': title,
            'form': CreateAluno(request.POST)
        }

        return render(
            request, 
            'tennisTracer/createAluno.html',
            context,
        )

    title = 'Cadastrar Novo Aluno'

    context = {
        'title': title,
        'form': CreateAluno
    }

    return render(
        request, 
        'tennisTracer/createAluno.html',
        context,
    )