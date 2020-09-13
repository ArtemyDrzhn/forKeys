from django.conf import settings
from django.db import models
from django.utils import timezone



class Users(models.Model):
    user=  models.CharField(max_length=30)
    is_manager = models.BooleanField(default=True)

class Questions(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

class Answers(models.Model):
    question = models.OneToOneField(Questions, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)

class Comments(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

class Categories(models.Model):
    question = models.ManyToManyField(Questions)
    categories = models.CharField(max_length=300)