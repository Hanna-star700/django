from django.db import models
from django.contrib.auth.models import User as DjangoUser

class Student(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, verbose_name="Користувач")
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    email = models.EmailField(verbose_name="Електронна пошта")
    age = models.IntegerField(verbose_name="Вік")
    created_at = models.DateTimeField(auto_now_add=True)
    is_registered = models.BooleanField(default=False, verbose_name="Зареєстрований")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

class QuizQuestion(models.Model):
    question_text = models.TextField(verbose_name="Текст питання")
    option_a = models.CharField(max_length=200, verbose_name="Варіант A")
    option_b = models.CharField(max_length=200, verbose_name="Варіант B")
    option_c = models.CharField(max_length=200, verbose_name="Варіант C")
    option_d = models.CharField(max_length=200, verbose_name="Варіант D")
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ], verbose_name="Правильна відповідь")
    category = models.CharField(max_length=50, verbose_name="Категорія")

    def __str__(self):
        return self.question_text[:50] + "..."

    class Meta:
        verbose_name = "Питання тесту"
        verbose_name_plural = "Питання тестів"

class QuizResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    score = models.IntegerField(verbose_name="Бал")
    total_questions = models.IntegerField(default=50, verbose_name="Загальна кількість питань")
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name="Завершено")
    recommendations = models.TextField(blank=True, verbose_name="Рекомендації")

    def __str__(self):
        return f"{self.student.name} - {self.score}/{self.total_questions}"

    class Meta:
        verbose_name = "Результат тесту"
        verbose_name_plural = "Результати тестів"

class VideoLesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    youtube_url = models.URLField(verbose_name="YouTube URL")
    duration = models.CharField(max_length=10, verbose_name="Тривалість")
    order = models.IntegerField(verbose_name="Порядок")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Відео урок"
        verbose_name_plural = "Відео уроки"

class QuizAttempt(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    score = models.IntegerField(verbose_name="Бал")
    total = models.IntegerField(verbose_name="Всього питань")
    percentage = models.FloatField(verbose_name="Відсоток")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    def __str__(self):
        return f"{self.name}: {self.score}/{self.total} ({round(self.percentage)}%)"

    class Meta:
        verbose_name = "Спроба тесту"
        verbose_name_plural = "Спроби тестів"