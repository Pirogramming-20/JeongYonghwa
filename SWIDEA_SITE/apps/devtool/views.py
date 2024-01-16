from django.shortcuts import render, redirect
from .forms import *
from .models import *

def show_list(request):
    tools = Devtool.objects.all()
    context = {
        'tools':tools
    }
    return render(request, 'devtool/devtool_list.html', context)

def create(request):
    if request.method == "POST":
        form = DevtoolRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool:list')
    form = DevtoolRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'devtool/devtool_register.html', context)

def detail(request, pk):
    tool = Devtool.objects.get(pk=pk)
    ideas = tool.idea_set.all()
    context = {
        'tool':tool,
        'ideas':ideas,
        'pk':pk,
    }
    return render(request, 'devtool/devtool_detail.html', context)

def delete(request, pk):
    if request.method == "POST":
        Devtool.objects.get(pk=pk).delete()
        return redirect('devtool:list')

def update(request, pk):
    tool = Devtool.objects.get(pk=pk)
    if request.method == "POST":
        form = DevtoolRegisterForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('devtool:detail', pk)
    form = DevtoolRegisterForm(instance=tool)
    context = {
        'form':form,
        'pk':pk,
    }
    return render(request, 'devtool/devtool_update.html', context)