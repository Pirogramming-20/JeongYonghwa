from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    # 추가) ModelForm은 Meta에서 명시된 model의 field와
    # 같은 Attr을 가지는 form 객체를 생성한다.

    class Meta:
        model = Post
        fields = ('title', 'text',)