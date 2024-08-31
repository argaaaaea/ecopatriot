from django.db import models
import uuid

# Create your models here.
class Roles(models.Model):
  roleName = models.CharField(max_length=256)
  id_pk = models.UUIDField(unique=True, default=uuid.uuid4)

class Users(models.Model):
  username = models.CharField(max_length=28, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=256)
  roleId = models.ForeignKey(Roles, on_delete=models.CASCADE)
  id_pk = models.UUIDField(unique=True, default=uuid.uuid4)
  
class Quizzes(models.Model):
  title = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  id_pk = models.UUIDField(unique=True, default=uuid.uuid4)

class Questions(models.Model):
  questionText = models.CharField()
  quizId = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
  id_pk = models.UUIDField(unique=True, default=uuid.uuid4)
  
class Answers(models.Model):
  answerText = models.CharField()
  isCorrect = models.BooleanField()
  questionId = models.ForeignKey(Questions, on_delete=models.CASCADE)
  id_pk = models.UUIDField(unique=True, default=uuid.uuid4)

class Results(models.Model):
  id_pk = models.UUIDField(default=uuid.uuid4, unique=True)
  score = models.IntegerField()
  takenAt = models.DateTimeField(auto_now_add=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  quizId = models.ForeignKey(Quizzes, on_delete=models.CASCADE)