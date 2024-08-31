from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from http import HTTPStatus
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Questions, Quizzes, Results, Answers, Roles
from django.forms.models import model_to_dict
import dashscope
from dashscope import Application
# Create your views here.

dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'

@csrf_exempt
def call_agent_api(request):
  body = json.loads(request.body)
  topics = body.get('topics')
  num_of_q = body.get('number_of_questions')
  response = Application.call(
    app_id="8070f070fb4142d0ad0b5cbf9bcfa21e",
    prompt=f"Tolong buatkan {num_of_q} pertanyaan seputar {topics}",
    api_key="sk-680812113955499b9a7dde188764e692"  
  )
  print(response.status_code)
  if response.status_code != HTTPStatus.OK:
      print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
      return JsonResponse({'output': 'gagal'})
  else:
    print(response.output)
    json_data = json.loads(f"[{response.output.text}]")
    return JsonResponse({'output': json_data})
  

def get_all_users(request):
  all_users = Users.objects.all()
  serialized_data = serializers.serialize('json', all_users)
  return JsonResponse(json.loads(serialized_data), safe=False)

def get_users_by_id(request, id_users):
  users = Users.objects.get(id=id_users)
  response_data = model_to_dict(users)
  return JsonResponse(json.loads(response_data), safe=False)

@csrf_exempt
def add_users(request):
  body = json.loads(request.body)
  role = Roles.objects.get(pk=body.get('roleId'))
  if role != None:
    new_users = Users.objects.create(username=body.get('username'), email=body.get('email'), password=body.get('password'), roleId=role)
  response_data = model_to_dict(Users.objects.get(pk=new_users.id))
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def update_users(request, id_users):
  body = json.loads(request.body)
  old_users = Users.objects.get(pk=id_users)
  if old_users:
    if body.get('username') != None:
      old_users.username = body.get('username')
    if body.get('email') != None:
      old_users.email = body.get('email')
  old_users.save()
  response_data = model_to_dict(old_users)
  return JsonResponse(response_data, safe=False)

def get_all_quiz(request):
  all_quiz = Quizzes.objects.all()
  serialized_data = serializers.serialize('json', all_quiz)
  return JsonResponse(json.loads(serialized_data), safe=False)

def get_one_quiz(request, id_quizzes):
  one_quiz = Quizzes.objects.get(pk=id_quizzes)
  response_data = model_to_dict(one_quiz)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def add_quiz(request):
  body = json.loads(request.body)
  new_quiz = Quizzes.objects.create(title=body.get('title'), description=body.get('description'))
  response_data = model_to_dict(new_quiz)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def update_quiz(request, id_quizzes):
  body = json.loads(request.body)
  old_quiz = Quizzes.objects.get(pk=id_quizzes)
  if old_quiz:
    if body.get('title') != None:
      old_quiz.title = body.get('title')
    if body.get('description') != None:
      old_quiz.description = body.get('description')
  old_quiz.save()    
  response_data = model_to_dict(old_quiz)
  return JsonResponse(response_data, safe=False)

def get_all_questions_based_on_quiz(request, id_quizzes):
  list_questions = list(Questions.objects.filter(quizId=id_quizzes))
  serialized_data = serializers.serialize('json', list_questions)
  return JsonResponse(json.loads(serialized_data), safe=False)

def get_one_questions(request, id_questions):
  questions = Questions.objects.get(pk=id_questions)
  response_data = model_to_dict(questions)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def add_questions(request):
  body = json.loads(request.body)
  quiz = Quizzes.objects.get(pk=body.get('quizId'))
  new_questions = Questions.objects.create(questionText=body.get("questionText"), quizId=quiz)
  response_data = model_to_dict(new_questions)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def update_questions(request, id_questions):
  body = json.loads(request.body)
  old_questions = Questions.objects.get(pk=id_questions)
  if old_questions:
    if body.get('questionText'):
      old_questions.questionText = body.get("questionText")
  old_questions.save()
  response_data = model_to_dict(old_questions)
  return JsonResponse(response_data, safe=False)

def get_all_answers_based_on_questions(request, id_questions):
  list_answers = list(Answers.objects.filter(questionId = id_questions))
  serialized_data = serializers.serialize('json', list_answers)  
  return JsonResponse(serialized_data, safe=False)

def get_one_answers(request, id_answers):
  answers = Answers.objects.get(pk=id_answers)
  response_data = model_to_dict(answers)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def add_answers(request):
  body = json.loads(request.body)
  questions = Questions.objects.get(pk=body.get('questionId'))
  new_answers = Answers.objects.create(answerText=body.get('answersText'), isCorrect=body.get("isCorrect"), questionId = questions)
  response_data = model_to_dict(new_answers)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def update_answers(request, id_answers):
  body = json.loads(request.body)
  old_answers = Answers.objects.get(pk=id_answers)
  if old_answers:
    if body.get('answerText'):
      old_answers.answerText = body.get('answerText')
    if body.get('isCorrect') != None:
      old_answers.isCorrect = body.get('isCorrect')
  old_answers.save()
  response_data = model_to_dict(old_answers)
  return JsonResponse(response_data, safe=False)

def get_all_result_based_on_users(request, id_users):
  list_result = list(Results.objects.filter(userId=id_users))
  serialized_data = serializers.serialize('json', list_result)
  return JsonResponse(serialized_data, safe=False)

def get_all_result_based_on_quizzes(request, id_quizzes):
  list_result = list(Results.objects.filter(quizId=id_quizzes))

  serialized_data = serializers.serialize('json', list_result)
  return JsonResponse(serialized_data, safe=False)

def get_one_results(request, id_results):
  results = Results.objects.get(pk=id_results)
  response_data = model_to_dict(results)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def add_results(request):
  body = json.loads(request.body)
  users = Users.objects.get(pk=body.get('id_users'))
  quizzes = Quizzes.objects.get(pk=body.get('id_quizzes'))
  new_results = Results.objects.create(score=body.get('score'),userId=users, quizId=quizzes)
  response_data = model_to_dict(new_results)
  return JsonResponse(response_data, safe=False)

@csrf_exempt
def update_results(request, id_results):
  body = json.loads(request.body)
  old_results = Results.objects.get(pk=id_results)
  if old_results:
    if body.get('score'):
      old_results.score = body.get('score')
  old_results.save()
  response_data = model_to_dict(old_results)
  return JsonResponse(response_data, safe=False)




  