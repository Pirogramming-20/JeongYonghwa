from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm

def show_main(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'posts': posts})

@csrf_exempt
@login_required
def create_comment(request):
    req_data = json.loads(request.body)
    post_id = req_data['post_id']
    user_id = req_data['author_id']
    content = req_data['content']
    target_post = Post.objects.get(id=post_id)
    comment_data = {
    'post': target_post,
    'author': User.objects.get(id=user_id),  
    'content': content,
    }
    Comment.objects.create(**comment_data)
    context = {
        'post':target_post,
    }
    html_content = render(request, 'comment_block.html', context).content.decode('utf-8')
    return JsonResponse({'html_content':html_content, 'post_id':post_id})

@csrf_exempt
@login_required
def delete_comment(request):
    req_data = json.loads(request.body)
    commmet_id = req_data['comment_id']
    post_id = req_data['post_id']
    target_comment = Comment.objects.get(id=commmet_id)
    target_comment.delete()
    context = {
        'post':Post.objects.get(id=post_id),
    }
    html_content = render(request, 'comment_block.html', context).content.decode('utf-8')
    return JsonResponse({'html_content':html_content, 'post_id':post_id})

@csrf_exempt
@login_required
def mark_like(request):
    req_data = json.loads(request.body)
    post_id = req_data['post_id']
    user = request.user
    target_post = Post.objects.get(id=post_id)

    if user in target_post.likes.all():
        target_post.likes.remove(user)
        target_post.like_count -= 1
        target_post.save()
        liked = False
    else:
        target_post.likes.add(user)
        target_post.like_count += 1
        target_post.save()
        liked = True

    like_count = target_post.like_count
    return JsonResponse({'post_id': post_id, 'liked': liked, 'like_count': like_count})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:main_page')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})