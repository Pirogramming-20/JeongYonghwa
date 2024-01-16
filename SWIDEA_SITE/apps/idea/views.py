from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *

def show_list(request):
    ideas = Idea.objects.all()
    context = {
        'ideas':ideas,
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