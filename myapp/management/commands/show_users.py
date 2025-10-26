from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Показує всіх користувачів та їх права'

    def handle(self, *args, **options):
        users = User.objects.all()
        
        if not users:
            self.stdout.write(self.style.WARNING('Немає користувачів'))
            return
        
        self.stdout.write('\n' + '='*80)
        self.stdout.write(self.style.SUCCESS('Список всіх користувачів:'))
        self.stdout.write('='*80 + '\n')
        
        for user in users:
            self.stdout.write(f'Користувач: {user.username}')
            self.stdout.write(f'  - Email: {user.email}')
            self.stdout.write(f'  - is_staff: {user.is_staff} (доступ до адмінки)')
            self.stdout.write(f'  - is_superuser: {user.is_superuser} (повні права)')
            self.stdout.write(f'  - is_active: {user.is_active}')
            self.stdout.write('-'*80)
        
        self.stdout.write(f'\nВсього користувачів: {users.count()}\n')

