from django.db import models
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField('教科名', max_length = 255)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    day = models.DateField('日付', default=timezone.now)   #timezone.now：現在時間の取得
    FirstPeriod = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='1限', related_name='FirstPeriod',default=1)
    SecondPeriod = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='2限', related_name='SecondPeriod', default=2)
    ThirdPeriod = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='3限', related_name='ThirdPeriod', default=3)
    FourthPeriod = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='4限', related_name='FourthPeriod', default=4)
    FifthPeriod = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='5限', related_name='FifthPeriod', default=5)
    SixthPeriod = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='6限', related_name='SixthPeriod', default=6)
    text = models.TextField('必要な物リスト')   #TextField : 複数行のテキスト入力行になる

    def __str__(self):
        return str(self.day)    #strでint型からstr型に変換