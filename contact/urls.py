from django.urls import path
from contact import views

app_name = 'tennisTracer'    

urlpatterns = [
    
    path('tennisTracer/', views.index, name='index'), #Alterar posteriormente
    path('tennisTracer/<int:contact_id>/', views.profile, name='profile'),

    path('tennisTracer/', views.profile, name='profile'),
    # Crud 
    # Create: Criar 
    path('tennisTracer/createTemas/', views.createTemaAula, name='createTemas'),
    path('tennisTracer/createAluno/', views.createAluno, name='createAluno'),
    path('tennisTracer/addAluno/<int:id>/', views.addAluno, name='addAluno'),
    path('tennisTracer/vinAluno/', views.vinAluno, name='vinAluno'),
    path('tennisTracer/aula/<int:aula_id>/alunos/', views.alunos_por_aula, name='alunos_por_aula'),
    path('tennisTracer/aula/presente/', views.registrar_presenca, name='registrar_presenca'),

    # Detail: Get
    path('tennisTracer/profileCoach/', views.profileCoach, name='profileCoach'),
    # Update: Atualizar
    # Delete
]