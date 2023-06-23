from django.db import models
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField('教科名', max_length = 255)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    day = models.DateField('日付', default=timezone.now)   #timezone.now：現在時間の取得
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT, verbose_name = '教科')
    text = models.TextField('必要な物')   #TextField : 複数行のテキスト入力行になる

    def __str__(self):
        return str(self.day)    #strでint型からstr型に変換