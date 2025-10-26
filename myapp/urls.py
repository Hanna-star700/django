from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start-learning/', views.start_learning, name='start_learning'),
    path('quiz/', views.quiz, name='quiz'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    path('quiz-results/', views.quiz_results, name='quiz_results'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('auth/', views.auth_page, name='auth'),
    path('video-lessons/', views.video_lessons, name='video_lessons'),
    path('lessons/', views.lessons, name='lessons'),
    path('tests/', views.tests, name='tests'),
    path('rating/', views.rating, name='rating'),
]