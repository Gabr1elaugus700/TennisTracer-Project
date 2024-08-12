from django import forms
from django.core.exceptions import ValidationError
from contact.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

class TennisTracerForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = (
            'tema_name',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'tema_name',
            ValidationError(
                'Mensagem de Erro', 
                code='invalid'
            )
        )
        return super().clean()

def create(request):
    if request.method == 'POST':

        title = 'Cadastrar Nova Aula'

        context = {
            'title': title,
            'form': TennisTracerForm(request.POST)
        }

        return render(
            request, 
            'tennisTracer/create.html',
            context,
        )

    title = 'Cadastrar Nova Aula'

    context = {
        'title': title,
        'form': TennisTracerForm
    }

    return render(
        request, 
        'tennisTracer/create.html',
        context,
    )