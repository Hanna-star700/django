from django.core.management.base import BaseCommand
from myapp.models import QuizQuestion, VideoLesson

class Command(BaseCommand):
    help = 'Додає приклади питань та відео уроків для демонстрації'

    def handle(self, *args, **options):
        # Очищаємо існуючі дані
        QuizQuestion.objects.all().delete()
        VideoLesson.objects.all().delete()
        
        # Додаємо приклади питань
        questions = [
            # Основи Python
            {
                'question_text': 'Який символ використовується для коментарів в Python?',
                'option_a': '//',
                'option_b': '#',
                'option_c': '/*',
                'option_d': '--',
                'correct_answer': 'B',
                'category': 'Основи'
            },
            {
                'question_text': 'Як створити змінну в Python?',
                'option_a': 'var name = "Python"',
                'option_b': 'name = "Python"',
                'option_c': 'string name = "Python"',
                'option_d': 'name := "Python"',
                'correct_answer': 'B',
                'category': 'Змінні'
            },
            {
                'question_text': 'Який тип даних має число 3.14?',
                'option_a': 'int',
                'option_b': 'float',
                'option_c': 'double',
                'option_d': 'decimal',
                'correct_answer': 'B',
                'category': 'Типи даних'
            },
            {
                'question_text': 'Що виведе print(type(10))?',
                'option_a': "<class 'integer'>",
                'option_b': "<class 'int'>",
                'option_c': "number",
                'option_d': "int",
                'correct_answer': 'B',
                'category': 'Типи даних'
            },
            {
                'question_text': 'Як правильно оголосити список в Python?',
                'option_a': 'list = {1, 2, 3}',
                'option_b': 'list = [1, 2, 3]',
                'option_c': 'list = (1, 2, 3)',
                'option_d': 'list = <1, 2, 3>',
                'correct_answer': 'B',
                'category': 'Списки'
            },
            {
                'question_text': 'Як отримати довжину рядка?',
                'option_a': 'str.length()',
                'option_b': 'len(str)',
                'option_c': 'str.size()',
                'option_d': 'str.count()',
                'correct_answer': 'B',
                'category': 'Рядки'
            },
            {
                'question_text': 'Що виведе print(2 + 3 * 2)?',
                'option_a': '10',
                'option_b': '8',
                'option_c': '12',
                'option_d': '7',
                'correct_answer': 'B',
                'category': 'Операції'
            },
            {
                'question_text': 'Яке ключове слово використовується для визначення функції?',
                'option_a': 'function',
                'option_b': 'def',
                'option_c': 'func',
                'option_d': 'define',
                'correct_answer': 'B',
                'category': 'Функції'
            },
            {
                'question_text': 'Що означає інтерпретована мова програмування?',
                'option_a': 'Код компілюється в машинний код',
                'option_b': 'Код виконується рядок за рядком',
                'option_c': 'Потрібен інтернет для роботи',
                'option_d': 'Код пишеться на двох мовах',
                'correct_answer': 'B',
                'category': 'Основи'
            },
            {
                'question_text': 'Як перевірити, чи є елемент у списку?',
                'option_a': 'list.contains(item)',
                'option_b': 'item in list',
                'option_c': 'list.has(item)',
                'option_d': 'list.find(item)',
                'correct_answer': 'B',
                'category': 'Списки'
            },
            # Умови та цикли
            {
                'question_text': 'Який оператор використовується для перевірки рівності?',
                'option_a': '=',
                'option_b': '==',
                'option_c': '===',
                'option_d': 'equals',
                'correct_answer': 'B',
                'category': 'Умови'
            },
            {
                'question_text': 'Що робить цикл while?',
                'option_a': 'Виконує код один раз',
                'option_b': 'Виконує код поки умова істинна',
                'option_c': 'Виконує код певну кількість разів',
                'option_d': 'Виконує код назавжди',
                'correct_answer': 'B',
                'category': 'Цикли'
            },
            {
                'question_text': 'Як записати умову "якщо x більше 5"?',
                'option_a': 'if x > 5:',
                'option_b': 'if (x > 5)',
                'option_c': 'if x > 5',
                'option_d': 'if x >= 5:',
                'correct_answer': 'A',
                'category': 'Умови'
            },
            {
                'question_text': 'Що виведе: for i in range(3): print(i)',
                'option_a': '1 2 3',
                'option_b': '0 1 2',
                'option_c': '0 1 2 3',
                'option_d': '1 2',
                'correct_answer': 'B',
                'category': 'Цикли'
            },
            {
                'question_text': 'Яка команда використовується для виходу з циклу?',
                'option_a': 'exit',
                'option_b': 'break',
                'option_c': 'stop',
                'option_d': 'end',
                'correct_answer': 'B',
                'category': 'Цикли'
            },
            # Рядки
            {
                'question_text': 'Що виведе print("Hello"[1])?',
                'option_a': 'H',
                'option_b': 'e',
                'option_c': 'l',
                'option_d': 'Error',
                'correct_answer': 'B',
                'category': 'Рядки'
            },
            {
                'question_text': 'Як об\'єднати два рядки "Hello" та "World"?',
                'option_a': '"Hello" + "World"',
                'option_b': '"Hello".join("World")',
                'option_c': 'concat("Hello", "World")',
                'option_d': '"Hello" & "World"',
                'correct_answer': 'A',
                'category': 'Рядки'
            },
            {
                'question_text': 'Що робить метод .upper()?',
                'option_a': 'Переводить рядок у нижній регістр',
                'option_b': 'Переводить рядок у верхній регістр',
                'option_c': 'Видаляє пробіли',
                'option_d': 'Реверсує рядок',
                'correct_answer': 'B',
                'category': 'Рядки'
            },
            # Списки та колекції
            {
                'question_text': 'Як додати елемент в кінець списку?',
                'option_a': 'list.add(item)',
                'option_b': 'list.append(item)',
                'option_c': 'list.insert(item)',
                'option_d': 'list.push(item)',
                'correct_answer': 'B',
                'category': 'Списки'
            },
            {
                'question_text': 'Що виведе print([1,2,3][1:3])?',
                'option_a': '[1, 2]',
                'option_b': '[2, 3]',
                'option_c': '[1, 2, 3]',
                'option_d': '[2]',
                'correct_answer': 'B',
                'category': 'Списки'
            },
            {
                'question_text': 'Який метод видаляє елемент зі списку?',
                'option_a': 'list.delete(item)',
                'option_b': 'list.remove(item)',
                'option_c': 'list.pop(item)',
                'option_d': 'list.discard(item)',
                'correct_answer': 'B',
                'category': 'Списки'
            },
            # Словники
            {
                'question_text': 'Як створити порожній словник?',
                'option_a': 'dict = []',
                'option_b': 'dict = {}',
                'option_c': 'dict = ()',
                'option_d': 'dict = set()',
                'correct_answer': 'B',
                'category': 'Словники'
            },
            {
                'question_text': 'Як отримати значення з словника за ключем "name"?',
                'option_a': 'dict[name]',
                'option_b': 'dict["name"]',
                'option_c': 'dict.name',
                'option_d': 'dict.get(name)',
                'correct_answer': 'B',
                'category': 'Словники'
            },
            # Функції
            {
                'question_text': 'Яке ключове слово повертає значення з функції?',
                'option_a': 'give',
                'option_b': 'return',
                'option_c': 'output',
                'option_d': 'result',
                'correct_answer': 'B',
                'category': 'Функції'
            },
            {
                'question_text': 'Що таке параметр функції?',
                'option_a': 'Результат функції',
                'option_b': 'Змінна яку передають у функцію',
                'option_c': 'Назва функції',
                'option_d': 'Тип даних',
                'correct_answer': 'B',
                'category': 'Функції'
            }
        ]
        
        for q_data in questions:
            QuizQuestion.objects.create(**q_data)
        
        # Додаємо приклади відео уроків
        videos = [
            {
                'title': 'Основи Python - Вступ',
                'description': 'Дізнайтеся про основи мови програмування Python, її історію та переваги',
                'youtube_url': 'https://www.youtube.com/watch?v=kqtD5dpn9C8',
                'duration': '10:30',
                'order': 1
            },
            {
                'title': 'Змінні та типи даних',
                'description': 'Навчіться працювати зі змінними та різними типами даних в Python',
                'youtube_url': 'https://www.youtube.com/watch?v=cQT33yu9pY8',
                'duration': '15:45',
                'order': 2
            },
            {
                'title': 'Умовні оператори',
                'description': 'Вивчіть як використовувати if, elif та else для прийняття рішень',
                'youtube_url': 'https://www.youtube.com/watch?v=AWek49wXGzI',
                'duration': '12:20',
                'order': 3
            },
            {
                'title': 'Цикли for та while',
                'description': 'Навчіться повторювати код за допомогою циклів for та while',
                'youtube_url': 'https://www.youtube.com/watch?v=OnDr4J2UXSA',
                'duration': '18:15',
                'order': 4
            },
            {
                'title': 'Функції в Python',
                'description': 'Дізнайтеся як створювати та використовувати функції для організації коду',
                'youtube_url': 'https://www.youtube.com/watch?v=9Os0o3wzS_I',
                'duration': '20:30',
                'order': 5
            }
        ]
        
        for v_data in videos:
            VideoLesson.objects.create(**v_data)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Успішно додано {len(questions)} питань та {len(videos)} відео уроків!'
            )
        )

