from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from contact.forms import CreateTemaAula, CreateAluno, AddAluno
from django.http import JsonResponse
import json


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

def vinAluno(request):
    if request.method == 'POST':
        print('To aqui')
        data = json.loads(request.body)
        aula_id = data.get('aula_id')
        aluno_id = data.get('aluno_id')

        aula = get_object_or_404(Aula, id=aula_id)
        aluno = get_object_or_404(Aluno, id=aluno_id)

        # Verifica se a relação já existe para evitar duplicatas
        vinculo_existente = Aluno_Aula.objects.filter(aula=aula, aluno=aluno).exists()

        if not vinculo_existente: 
            Aluno_Aula.objects.create(aula=aula, aluno=aluno)
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'duplicate'}, status=400)
    
    return JsonResponse({'status': 'invalid method'}, status=405)