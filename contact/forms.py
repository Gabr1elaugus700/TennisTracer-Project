from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.models import User

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


    # def clean(self): #Validando campo que depende de outro campo e é chamado antes de Salvar no BD
    #     cleaned_data = self.cleaned_data
        
    #     self.add_error(
    #         'tema_name',
    #         ValidationError(
    #             'Descreva o Tema, Por Favor!', 
    #             code='invalid'
    #         )
    #     )
    #     return super().clean()
    

    ## Esse é o Clean do Campo, ele executa primeiro que o de cima!
    
    # def clean_tema_name(self):
    #     tema_name = self.cleaned_data.get('tema_name')
        
    #     if tema_name:
    #         self.add_error(
    #             'tema_name',
    #             ValidationError(
    #                 'Erro Aqui. Não digite ABC',
    #                 code='invalid'
    #             )
    #         )
    #     return tema_name

class CreateAluno(forms.ModelForm):

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

    old = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Informe a idade do aluno'
            }
        ),
        label='Idade:',
        help_text='Ex: 4'
    )

    birthday = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y',  # Formato brasileiro
            attrs={
                'placeholder': 'dd/mm/aaaa',  # Formato de data esperado
                'type': 'text'  # Muda para 'text' para exibir o formato personalizado
            }
        ),
        label='Data de Nascimento',
        help_text='Ex: 31/12/2000'
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
        choices=[(user.id, user.username) for user in User.objects.all()],
        widget=forms.Select(
            attrs={
                'class': 'form-group',
                'placeholder': 'Escolha'
            }
        ),
        label='Escolha o Tipo do Usuário:',
        help_text='Escolha uma das opções'
    )

    def clean_owner(self):
        owner_id = self.cleaned_data.get('owner')

        # Verifica se o usuário com o ID existe
        try:
            owner = User.objects.get(id=owner_id)
        except User.DoesNotExist:
            raise ValidationError('Usuário inválido.')

        return owner

    class Meta:
        model = models.Aluno  # Associa o formulário ao modelo Aluno
        fields = ('first_name', 'last_name', 'old' , 'login', 'owner')
    
