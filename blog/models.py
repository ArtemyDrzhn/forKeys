from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Persons(models.Model):
    name_person=  models.CharField(max_length=30)
    is_manager = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_persons(sender, instance, created, **kwargs):
        if created:
            Persons.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.persons.save()
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Categories(models.Model):
    name_cat = models.CharField(max_length=300)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Questions(models.Model):
    name_person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    name_cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answers(models.Model):
    ask = models.OneToOneField(Questions, on_delete=models.CASCADE, primary_key=True)
    name_person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Comments(models.Model):
    ask = models.ForeignKey(Questions, on_delete=models.CASCADE)
    name_person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

