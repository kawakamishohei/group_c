from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Userモデルにないフィールドを追加している
    age = models.PositiveIntegerField('年齢')

    REQUIRED_FIELDS = ['age']

    def __str__(self):
        return age


class UserAge(models.Model):
    name = models.CharField('年齢', max_length=255)

    def __str__(self):
        return self.name
# Create your models here.
