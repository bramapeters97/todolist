from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.shortcuts import render, get_object_or_404
from .forms import TodoForm
from django.shortcuts import redirect

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(deadline_date__lte=timezone.now()).order_by('deadline_date')
    return render(request, 'list/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'list/todo_detail.html', {'todo': todo})

def todo_new(request):
    todo = TodoForm()
    return render(request, 'list/todo_edit.html', {'todo': todo})

def todo_new(request):
    if request.method == "POST":
        todo = TodoForm(request.POST)
        if todo.is_valid():
            todo = todo.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        todo = TodoForm()
    return render(request, 'list/todo_edit.html', {'todo': todo})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo = TodoForm(request.POST, instance=todo)
        if todo.is_valid():
            todo = todo.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        todo = TodoForm()
    return render(request, 'list/todo_edit.html', {'todo': todo})
