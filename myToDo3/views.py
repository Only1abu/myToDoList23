from django.shortcuts import render, redirect
from .models import myToDo3
# Create your views here.
def index(request):
    todo = myToDo3.objects.all()

    if request.method == 'POST':
        new_todo = myToDo3(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {'todo': todo})

def delete(request, pk):
    todo= myToDo3.objects.get(id=pk)
    todo.delete()
    return redirect('/')

