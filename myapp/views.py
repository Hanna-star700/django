from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student, QuizQuestion, QuizResult, VideoLesson, QuizAttempt

def home(request):
    context = {
        'total_lessons': 10,
        'total_exercises': 25,
        'total_users': 150,
    }
    return render(request, 'home.html', context)

def start_learning(request):
    """Почати вивчення - перенаправлення на тест"""
    return redirect('quiz')

def quiz(request):
    """Вступний тест"""
    questions = QuizQuestion.objects.all()  
    context = {
        'questions': questions,
        'total_questions': len(questions)
    }
    return render(request, 'quiz.html', context)

@csrf_exempt
def submit_quiz(request):
    """Обробка результатів тесту"""
    if request.method == 'POST':
        data = json.loads(request.body)
        answers = data.get('answers', {})
        name = (data.get('name') or '').strip() or 'Гість'
        
        # Підрахунок правильних відповідей
        correct_count = 0
        total_questions = QuizQuestion.objects.count()  # Загальна кількість питань в базі
        wrong_categories = {}
        
        for question_id, answer in answers.items():
            try:
                question = QuizQuestion.objects.get(id=question_id)
                if answer == question.correct_answer:
                    correct_count += 1
                else:
                    # накопичуємо категорії неправильних відповідей
                    cat = (question.category or 'Основи')
                    wrong_categories[cat] = wrong_categories.get(cat, 0) + 1
            except QuizQuestion.DoesNotExist:
                continue
        
        # Створення анонімного результату
        percentage = (correct_count / total_questions * 100) if total_questions > 0 else 0
        topics_to_review = [c for c, _ in sorted(wrong_categories.items(), key=lambda x: x[1], reverse=True)[:3]]
        # Досягнення
        if percentage >= 80:
            achievement = '🏆 Gold: Відмінний старт!'
        elif percentage >= 60:
            achievement = '⭐ Silver: Гарний результат'
        elif percentage >= 40:
            achievement = '🎖️ Bronze: Є прогрес'
        else:
            achievement = '🌱 Newbie: Початок шляху'

        # Зберегти спробу для рейтингу
        try:
            QuizAttempt.objects.create(
                name=name,
                score=correct_count,
                total=total_questions,
                percentage=percentage,
            )
        except Exception:
            pass

        result = {
            'name': name,
            'score': correct_count,
            'total': total_questions,
            'percentage': percentage,
            'achievement': achievement,
            'topics': topics_to_review,
        }
        
        # Генерація рекомендацій
        recommendations = generate_recommendations(correct_count, total_questions)
        result['recommendations'] = recommendations
        
        return JsonResponse(result)

def generate_recommendations(score, total):
    """Генерація рекомендацій на основі результатів"""
    percentage = (score / total * 100) if total > 0 else 0
    
    if percentage >= 80:
        return "Відмінно! Ви маєте хороші базові знання. Рекомендуємо продовжити з розширеними темами Python."
    elif percentage >= 60:
        return "Добре! У вас є базові знання, але варто повторити основи програмування та синтаксис Python."
    elif percentage >= 40:
        return "Потрібно більше практики з основами. Рекомендуємо почати з базових концепцій програмування."
    else:
        return "Рекомендуємо почати з нуля з основ програмування та Python. Не поспішайте, важливо засвоїти фундаментальні концепції."

def quiz_results(request):
    """Сторінка результатів тесту"""
    return render(request, 'quiz_results.html')

def register(request):
    return redirect('auth')

@login_required
def video_lessons(request):
    """Сторінка з відео уроками"""
    lessons = VideoLesson.objects.all().order_by('order')
    context = {
        'lessons': lessons
    }
    return render(request, 'video_lessons.html', context)

def lessons(request):
    lessons_data = [
        {'id': 1, 'title': 'Основи Python', 'description': 'Змінні, типи даних, операції', 'progress': 100},
        {'id': 2, 'title': 'Умови', 'description': 'if, elif, else statements', 'progress': 80},
        {'id': 3, 'title': 'Цикли', 'description': 'for, while loops', 'progress': 60},
        {'id': 4, 'title': 'Функції', 'description': 'Створення та використання функцій', 'progress': 40},
        {'id': 5, 'title': 'Списки', 'description': 'Робота з колекціями даних', 'progress': 20},
        {'id': 6, 'title': 'Словники', 'description': 'Key-value структури даних', 'progress': 0},
    ]
    return render(request, 'lessons.html', {'lessons': lessons_data})

def tests(request):
    if request.method == 'POST':
        # Правильні відповіді для тесту
        correct_answers = {
            'q1': 'b',  # 2 + 3 * 2 = 2 + 6 = 8
            'q2': 'a',  # "Hello"[1:4] = "ell"
            'q3': 'a',  # Перевіряє чи перший елемент 5
            'q4': 'b',  # type(3.14) = float
            'q5': 'b',  # len([1,2,3,4]) = 4
        }
        
        # Підрахунок правильних відповідей
        score = 0
        total = len(correct_answers)
        
        for question, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question)
            if user_answer == correct_answer:
                score += 1
        
        percentage = (score / total * 100) if total > 0 else 0
        
        # Генерація повідомлення
        if percentage >= 80:
            message = "Відмінно! 🏆"
            level = "success"
        elif percentage >= 60:
            message = "Добре! ⭐"
            level = "info"
        elif percentage >= 40:
            message = "Непогано! 🎖️"
            level = "warning"
        else:
            message = "Потрібно більше практики 📚"
            level = "error"
        
        # Зберігаємо результат в сесії для показу на сторінці
        request.session['test_result'] = {
            'score': score,
            'total': total,
            'percentage': round(percentage, 1),
            'message': message,
            'level': level
        }
        
        return redirect('tests')
    
    # GET запит - показуємо форму та результати якщо є
    result = request.session.pop('test_result', None)
    return render(request, 'tests.html', {'result': result})

def rating(request):
    attempts = QuizAttempt.objects.all().order_by('-percentage', '-created_at')[:20]
    return render(request, 'rating.html', {'attempts': attempts})

def login_view(request):
    return redirect('auth')

def logout_view(request):
    logout(request)
    messages.info(request, 'Ви вийшли з облікового запису.')
    return redirect('home')

def auth_page(request):
    login_form = AuthenticationForm(request, data=request.POST or None)
    register_form = UserCreationForm(request.POST or None)
    
    # Визначаємо який таб показати
    show_register = request.GET.get('tab') == 'register' or request.POST.get('form_type') == 'register'

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'login':
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, 'Вхід виконано успішно!')
                return redirect('home')
        elif form_type == 'register':
            if register_form.is_valid():
                user = register_form.save(commit=False)
                # Переконуємося що звичайний користувач НЕ має доступу до адмінки
                user.is_staff = False
                user.is_superuser = False
                user.save()
                Student.objects.create(
                    user=user,
                    name=user.username,
                    email=user.email or '',
                    age=0,
                    is_registered=True
                )
                login(request, user)
                messages.success(request, 'Реєстрація успішна!')
                return redirect('video_lessons')

    return render(request, 'auth.html', {
        'login_form': login_form,
        'register_form': register_form,
        'show_register': show_register,
    })