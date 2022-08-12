from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='loginpage')
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "todo/homepage.html", {'tasks': tasks})


@login_required(login_url='loginpage')
def add(request):
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user_id = request.user.id
            new_task.save()
            return redirect('home')
    return render(request, 'todo/addpage.html', {'form': form})


@login_required(login_url='loginpage')
def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # form = TaskForm

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')
    return render(request, 'todo/editpage.html', {'task': task})


@login_required(login_url='loginpage')
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        task.delete()
        return redirect('home')


'''
def done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        task.completed = True
        return redirect('home')
'''