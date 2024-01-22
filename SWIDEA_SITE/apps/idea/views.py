from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *

def show_list(request):
    ideas = Idea.objects.all()
    paginator = Paginator(ideas, 4)
    page = request.GET.get('page')
    if not page or int(page) < 1:
        page = 1
    elif int(page) > paginator.num_pages:
        page = paginator.num_pages
    page_obj = paginator.page(page)
    context = {
        'ideas':ideas,
        'page_obj':page_obj,
        'paginator':paginator
    }
    return render(request, 'idea/idea_list.html', context)

def create(request):
    if request.method == "POST":
        form = IdeaRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea:main_page')
    form = IdeaRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'idea/idea_register.html', context)

def update(request, pk):
    idea = Idea.objects.get(pk=pk)
    if request.method == "POST":
        form = IdeaRegisterForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea:detail', pk)
    form = IdeaRegisterForm(instance=idea)
    context = {
        'form':form,
        'pk':pk,
    }
    return render(request, 'idea/idea_update.html', context)

def delete(request, pk):
    if request.method == "POST":
        Idea.objects.get(pk=pk).delete()
    return redirect('idea:main_page')

def detail(request, pk):
    idea = Idea.objects.get(pk=pk)
    context = {
        'idea':idea
    }
    return render(request, 'idea/idea_detail.html', context)

def change_marked(request, pk):
    idea = Idea.objects.get(pk=pk)
    idea.marked = not idea.marked
    idea.save()
    return JsonResponse({'marked': idea.marked})

def change_order(request, criterion):
    ideas = Idea.objects.order_by(criterion)
    paginator = Paginator(ideas, 4)
    page = request.GET.get('page')
    if not page or int(page) < 1:
        page = 1
    elif int(page) > paginator.num_pages:
        page = paginator.num_pages
    page_obj = paginator.page(page)
    context = {
        'ideas':ideas,
        'page_obj':page_obj,
        'paginator':paginator,
        'criterion':criterion,
    }
    return render(request, 'idea/idea_list.html', context)

def increase_interest(request, pk):
    idea = Idea.objects.get(pk=pk)
    idea.interest += 1
    idea.save()
    return JsonResponse({'interest':idea.interest})

def decrease_interest(request, pk):
    idea = Idea.objects.get(pk=pk)
    idea.interest -= 1
    idea.save()
    return JsonResponse({'interest':idea.interest})