from django.urls import path
from contact import views

app_name = 'tennisTracer'    

urlpatterns = [
    path('tennisTracer/', views.index, name='index'),
    path('tennisTracer/<int:contact_id>/', views.profile, name='profile'),

    path('tennisTracer/', views.profile, name='profile'),
    # Crud 
    path('tennisTracer/create/', views.create, name='create'),
    # Detail: Get
    # Create: Criar 
    # Update: Atualizar
    # Delete


]