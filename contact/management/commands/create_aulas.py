from django.core.management.base import BaseCommand
from datetime import time
from django.core.exceptions import ObjectDoesNotExist
from contact.models import Aula, Coach

class Command(BaseCommand):
    help = 'Cria aulas de segunda a sábado, excluindo horário de almoço'

    def handle(self, *args, **kwargs):
        dias_da_semana = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
        horarios = [
            time(hour=8), time(hour=9), time(hour=10), time(hour=11),
            time(hour=13), time(hour=14), time(hour=15), time(hour=16), time(hour=17)
        ]

        try:
            coach = Coach.objects.get(id=1)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR('Nenhum coach com ID 1 encontrado.'))
            return

        for dia in dias_da_semana:
            for hora in horarios:
                Aula.objects.create(
                    day=dia, 
                    hora_ini=hora, 
                    hora_fim=(time(hora.hour + 1)),
                    coach=coach
                )
        
        self.stdout.write(self.style.SUCCESS('Aulas criadas com sucesso!'))
