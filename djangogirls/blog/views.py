from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# blog.urls를 통해 매칭되는 view를 찾아 request를 넘김
# view는 request를 받아서 처리하고 결과를 보냄