from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    # Userモデルにないフィールドを追加している
    age = models.PositiveIntegerField('年齢')

    REQUIRED_FIELDS = ['age']

# Create your models here.
