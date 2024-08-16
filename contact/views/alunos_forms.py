from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from contact.forms import CreateTemaAula, CreateAluno, AddAluno


def createTemaAula(request):
    if request.method == 'POST':

        title = 'Cadastrar Nova Aula'
        form = CreateTemaAula(request.POST)

        context = {
            'title': title,
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('tennisTracer:createTemas')
        
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
        form = CreateAluno(request.POST)
        
        context = {
            'title': title,
            'form': form
        }

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            old = form.cleaned_data['old']
            birthday = form.cleaned_data['birthday']
            login = form.cleaned_data['login']
            owner = form.cleaned_data['owner']  # Já é uma instância de User

            # Crie ou atualize o objeto Aluno
            aluno = Aluno.objects.create(
                first_name=first_name,
                last_name=last_name,
                old=old,
                birthday=birthday,
                login=login,
                owner=owner
            )
            form.save()
            return redirect('tennisTracer:createAluno')

        return render(
            request, 
            'tennisTracer/createAluno.html',
            context,
        )

    title = 'Cadastrar Novo Aluno'
    form = CreateAluno()

    context = {
        'title': title,
        'form': form
    }

    return render(
        request, 
        'tennisTracer/createAluno.html',
        context,
    )

def addAluno(request, id):
    aula = get_object_or_404(Aula, id=id)
    alunos = Aluno.objects.all()

    if request.method == 'POST':
        form = AddAluno(request.POST)

        context = {
        'aula': aula,
        'alunos': alunos,
        'id': id
    }
    
        if form.is_valid():
           aluno = form.cleaned_data['aluno']
           Aluno_Aula.objects.create(aula=aula, aluno=aluno)
           return redirect('tennisTracer:index', id=id)
    
    form = AddAluno()
    print(id)

    context = {
        'form': form,
        'aula': aula,
        'alunos': alunos,
        'id': id
    }
    return render(
        request,
        'tennisTracer/teste.html', 
        context
        )