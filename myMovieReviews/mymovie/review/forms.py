from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        labels = {
            'title' : '제목',
            'release_date' : '개봉년도',
            'genre' : '장르',
            'score' : '별점',
            'showtime' : '러닝타임',
            'content' : '리뷰\n',
            'director' : '감독',
            'cast': '출연',
            'image': '이미지',
        }