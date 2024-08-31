from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_all_users, name='all_users'),
    path('users/add', views.add_users, name='add_users'),
    path('users/<int:id_users>', views.get_users_by_id, name='get_users'),
    path('users/update/<int:id_users>', views.update_users, name="update_users"),
    path('quizzes/', views.get_all_quiz, name="all_quizzes"),
    path('quizzes/add', views.add_quiz, name="add_quizzes"),
    path('quizzes/<int:id_quizzes>', views.get_one_quiz, name="get_quizzes"),
    path("quizzes/update/<int:id_quizzes>", views.update_quiz, name="update_quizzes"),
    path("quizzes/questions/<int:id_quizzes>", views.get_all_questions_based_on_quiz, name="all_questions"),
    path("questions/<int:id_questions>", views.get_one_questions, name="get_questions"),
    path("questions/add", views.add_questions, name="add_questions"),
    path("questions/update/<int:id_questions>", views.update_questions, name="update_questions"),
    path("questions/answers/<int:id_questions>", views.get_all_answers_based_on_questions, name="all_answers"),
    path("answers/<int:id_answers>", views.get_one_answers, name="get_answers"),
    path("answers/add", views.add_answers, name="add_answers"),
    path("answers/update/<int:id_answers>", views.update_answers, name="update_answers"),
    path("quizzes/results/<int:id_quizzes>", views.get_all_result_based_on_quizzes, name="all_results"),
    path("users/results/<int:id_users>", views.get_all_result_based_on_users, name="all_results"),
    path("results/<int:id_results>", views.get_one_results, name="get_results"),
    path("results/add", views.add_results, name="add_results"),
    path("results/update/<int:id_results>", views.update_results, name="update_results"),
    path("generate_questions", views.call_agent_api, name="generate_questions")
    
]
