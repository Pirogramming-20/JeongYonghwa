from django.db import models
from apps.devtool.models import Devtool

class Idea(models.Model):

    name = models.CharField('아이디어명', max_length=50)
    image = models.ImageField('이미지', null=True, upload_to='posts/')
    content = models.TextField('설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name = '예상 개발툴')
    marked  = models.BooleanField(default=False)