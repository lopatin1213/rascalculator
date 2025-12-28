from django.core.management.base import BaseCommand
from datetime import date
from for_adm.models import UserPro

class Command(BaseCommand):
    help = 'Удаляет пользователей с истекшим сроком PRO'

    def handle(self, *args, **options):
        today = date.today()
        # Только пользователи с установленной датой истечения и уже истекшими сроками
        expired_users = UserPro.objects.filter(pro_expiration_date__isnull=False, pro_expiration_date__lt=today)
        count = expired_users.count()
        expired_users.delete()
        self.stdout.write(self.style.SUCCESS(f'Удалено {count} пользователей с истекшим статусом PRO.'))