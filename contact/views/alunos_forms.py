from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
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


def detalhes_aula(request, aula_id):
    # Buscar a aula específica
    aula = get_object_or_404(Aula, id=aula_id)
    
    # Buscar os alunos vinculados a essa aula
    alunos_aula = Aluno_Aula.objects.filter(aula=aula)
    
    context = {
        'aula': aula,
        'alunos_aula': alunos_aula,
    }
    
    return render(request, 'day.html', context)

def alunos_por_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    alunos_aula = Aluno_Aula.objects.filter(aula=aula)


    alunos = []
    for aluno_aula in alunos_aula:
        aluno = aluno_aula.aluno
        alunos.append({
            'id': aluno.id,
            'first_name': aluno.first_name,
            'last_name': aluno.last_name,
            'picture': aluno.picture.url if aluno.picture else None
        })

    return JsonResponse({'alunos': alunos})

def registrar_presenca(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        aula_id = data.get('aula_id')
        alunos_ids = data.get('alunos', [])

        try:
            # Verificar se a aula existe
            aula = Aula.objects.get(id=aula_id)
            
            # Para cada aluno selecionado, atualizar a presença
            for aluno_id in alunos_ids:
                aluno_aula = Aluno_Aula.objects.get(aula=aula, aluno_id=aluno_id)
                aluno_aula.presente = True  # Supondo que você tenha um campo 'presente' no model
                aluno_aula.save()

            return JsonResponse({'status': 'success'})

        except Aula.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Aula não encontrada.'}, status=400)
        except Aluno_Aula.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Aluno não encontrado.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'}, status=400)