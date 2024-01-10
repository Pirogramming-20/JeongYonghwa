from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# blog.urls를 통해 매칭되는 view를 찾아 request를 넘김
# view는 request를 받아서 처리하고 결과를 보냄

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 모델(Table) Post에서 기본키 = pk값에 해당하는 값을
    # 탐색하고, 없으면 Page not found를 반환하라
    return render(request, 'blog/post_detail.html', {'post':post})