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
    path('tennisTracer/<int:aula_id>/addAluno/', views.addAluno, name='addAluno'),
    # Detail: Get
    path('tennisTracer/profileCoach/', views.profileCoach, name='profileCoach'),

    # Update: Atualizar
    # Delete


]