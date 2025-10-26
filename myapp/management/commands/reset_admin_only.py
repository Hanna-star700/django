from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Встановлює права адміністратора ТІЛЬКИ для користувача admin'

    def handle(self, *args, **options):
        users = User.objects.all()
        
        fixed_count = 0
        admin_found = False
        
        for user in users:
            if user.username == 'admin':
                # Переконуємось що admin має всі права
                if not user.is_staff or not user.is_superuser:
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Відновлено права для admin')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Користувач admin має правильні права')
                    )
                admin_found = True
            else:
                # Всі інші користувачі НЕ мають доступу до адмінки
                if user.is_staff or user.is_superuser:
                    user.is_staff = False
                    user.is_superuser = False
                    user.save()
                    fixed_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'✗ Видалено права адміністратора у: {user.username}')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Користувач {user.username} має правильні права (без доступу до адмінки)')
                    )
        
        if not admin_found:
            self.stdout.write(
                self.style.ERROR('\n⚠ УВАГА: Користувач "admin" не знайдений!')
            )
        
        self.stdout.write('\n' + '='*80)
        if fixed_count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'Виправлено {fixed_count} користувачів')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Всі користувачі мають правильні права!')
            )
        self.stdout.write('='*80 + '\n')

