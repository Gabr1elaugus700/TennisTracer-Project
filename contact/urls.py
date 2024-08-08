from django.urls import path
from contact import views

app_name = 'contact'    

urlpatterns = [
    path('index/', views.index, name='index'),
    path('profile/<int:contact_id>/', views.profile, name='profile'),

    path('aulas/', views.profile, name='profile'),
    # Crud 
    # Detail: Get
    # Create: Criar 
    # Update: Atualizar
    # Delete


]