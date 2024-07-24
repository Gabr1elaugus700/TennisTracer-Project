from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('teste/', views.index, name='index'),
]