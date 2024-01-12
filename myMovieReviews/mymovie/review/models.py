from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):

    Genre_Choices = (
        ('불명', '불명'),
        ('미스테리', '미스테리'),
        ('로맨스', '로맨스'),
        ('스릴러', '스릴러'),
        ('판타지', '판타지'),
        ('SF', 'SF'),
        ('액션', '액션'),
        ('느와르', '느와르'),
        ('스포츠', '스포츠'),
        ('코미디', '코미디'),
        ('전쟁', '전쟁'),
        ('호러', '호러'),
        ('음악', '음악'),
    )

    title = models.CharField(max_length = 32)
    release_date = models.IntegerField()
    genre = models.CharField(
        choices = Genre_Choices,
        default = ('불명', '불명'),
        max_length = 16
    )
    score = models.DecimalField(
        max_digits = 2,
        decimal_places = 1,
        validators = [
            MinValueValidator(limit_value=0),
            MaxValueValidator(limit_value=5)
        ]
    )
    showtime = models.IntegerField()
    content = models.TextField()
    director = models.CharField(max_length = 16)
    cast = models.CharField(max_length = 50)
