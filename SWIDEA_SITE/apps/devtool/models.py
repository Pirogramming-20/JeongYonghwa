from django.db import models

class Devtool(models.Model):
    name = models.CharField('이름', max_length = 20)
    kind = models.CharField('종류', max_length = 20)
    content = models.TextField('설명')

    def __str__(self):
        return self.name