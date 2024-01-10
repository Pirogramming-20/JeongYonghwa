from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts', posts})

# blog.urls를 통해 매칭되는 view를 찾아 request를 넘김
# view는 request를 받아서 처리하고 결과를 보냄