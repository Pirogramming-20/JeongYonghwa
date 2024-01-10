from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # 새로운 post 객체를 만들되 Post Model에 바로 저장하지 않음
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # PostForm은 Meta 정보에 명시된대로 Post 모델을 사용하고
            # 두 개의 속성에 대한 입력을 받아 처리한다
            # PostForm 객체는 Post 모델에 추가될 객체로 기능하며
            # 이때 생성된 post instance는 save() 메서드를 가진다
            # save()가 실행되는 시점에서, Post model은 post가 가진
            # 필드값에 맞는 레코드를 객체로 저장한다(Model명.objects로 접근)
            return redirect('post_detail', pk=post.pk)
            # save()가 실행되는 시점에서 pk값이 자동으로 저장되므로, 
            # 앞선 코드에서 생성된 post의 pk 값을 바로 참조할 수 있다
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    # 수정하길 원하는 페이지를 명시해야하므로 pk 값을 같이 가져간다
    post = get_object_or_404(Post, pk=pk)
    # request.method == POST인 경우 => submit 버튼을 누른 경우
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        # instance = 수정할 대상이 되는 post를 지정해줌
        # Update 기능을 구현할 때 쓰라고 제공하는 기능

        # request.POST라는 게 무엇인가?
        # 유저가 제출한 정보가 담긴 Dict 객체
        # -> ModelForm class를 Dict를 parameter로 받아 form 객체를 생성한다
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    # request가 POST가 아닐때 => 버튼을 처음 눌렀을 때
        # 수정 페이지로 가도록 html을 render해줌
    return render(request, 'blog/post_edit.html', {'form': form})