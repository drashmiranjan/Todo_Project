from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    todos = Todo.objects.all()
    d = {'todos': todos}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        TO = Todo(title=title, desc=desc)
        TO.save()
    return render(request, 'home.html', d)