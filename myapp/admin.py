from django.contrib import admin
from .models import Student, QuizQuestion, QuizResult, VideoLesson, QuizAttempt

admin.site.register(Student)
admin.site.register(QuizQuestion)
admin.site.register(QuizResult)
admin.site.register(VideoLesson)
admin.site.register(QuizAttempt)