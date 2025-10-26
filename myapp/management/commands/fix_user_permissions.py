from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Видаляє права адміністратора у всіх звичайних користувачів (окрім суперюзерів)'

    def handle(self, *args, **options):
        # Отримуємо всіх користувачів
        users = User.objects.all()
        
        fixed_count = 0
        for user in users:
            # Пропускаємо суперюзерів (тих хто створений через createsuperuser)
            if user.is_superuser:
                self.stdout.write(f'Пропущено суперюзера: {user.username}')
                continue
            
            # Якщо користувач має права адміністратора, але не є суперюзером
            if user.is_staff or user.is_superuser:
                user.is_staff = False
                user.is_superuser = False
                user.save()
                fixed_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Видалено права адміністратора у: {user.username}')
                )
        
        if fixed_count == 0:
            self.stdout.write(
                self.style.WARNING('Не знайдено користувачів з неправильними правами')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'\nУспішно виправлено {fixed_count} користувачів!')
            )

