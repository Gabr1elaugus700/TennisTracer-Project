from django import forms
from django.core.exceptions import ValidationError
from . import models

class CreateTemaAula(forms.ModelForm):
    
    #### Em um Form, atualiza As info Html do mesmo; 
    tema_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
             'placeholder': 'Digite aqui'
            }
        ),
        label='Informe a Descrição do tema:',
        help_text='Ex: BackHand'
    )

    class Meta:
        model = models.Tema
        fields = (
            'tema_name',
        )
        
        widgets = {
            'tema_name': forms.TextInput(
                
            )
        }


    def clean(self): #Validando campo que depende de outro campo e é chamado antes de Salvar no BD
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'tema_name',
            ValidationError(
                'Descreva o Tema, Por Favor!', 
                code='invalid'
            )
        )
        return super().clean()
    

    ## Esse é o Clean do Campo, ele executa primeiro que o de cima!
    
    def clean_tema_name(self):
        tema_name = self.cleaned_data.get('tema_name')
        
        if tema_name == 'ABC':
            self.add_error(
                'tema_name',
                ValidationError(
                    'Erro Aqui. Não digite ABC',
                    code='invalid'
                )
            )
        return tema_name

class CreateAluno(forms.ModelForm):
    
    #### Em um Form, atualiza As info Html do mesmo; 
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
             'placeholder': 'Digite o nome'
            }
        ),
        label='Nome Do Aluno',
        help_text='Ex: Camila'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
             'placeholder': 'Digite o sobrenome'
            }
        ),
        label='Sobrenome do Aluno:',
        help_text='Ex: Oliveira'
    )

    login = forms.CharField(
        widget=forms.TextInput(
            attrs={
             'placeholder': 'Digite o Login'
            }
        ),
        label='Login:',
        help_text='Ex: camila.oliveira'
    )

    owner = forms.ChoiceField(
        choices=[('Camila', 'Professora'), ('Gabriel', 'Aluno')], # O segundo valor, é o que de fato aparece no front
        widget=forms.Select(
            attrs={
                'class': 'form-group',
                'placeholder': 'Escolha'
            }
        ),
        label='Escolha o Tipo do Usuário:',
        help_text='Escolha uma das opções'
    )

    class Meta:
        model = models.Aluno
        fields = (
            'first_name', 'last_name', 'login', 'owner',
        )
        
        


    def clean(self): #Validando campo que depende de outro campo e é chamado antes de Salvar no BD
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Descreva o Tema, Por Favor!', 
                code='invalid'
            )
        )
        return super().clean()
    

    ## Esse é o Clean do Campo, ele executa primeiro que o de cima!
    
    def clean_tema_name(self):
        tema_name = self.cleaned_data.get('tema_name')
        
        if tema_name == 'ABC':
            self.add_error(
                'tema_name',
                ValidationError(
                    'Erro Aqui. Não digite ABC',
                    code='invalid'
                )
            )
        return tema_name
    
