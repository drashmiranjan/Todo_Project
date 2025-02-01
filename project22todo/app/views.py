from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from  django.urls import reverse
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


def update(request, pk):
    Tobj = Todo.objects.get(pk=pk)
    d = {'Tobj':Tobj}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        Tobj.title = title
        Tobj.desc = desc
        Tobj.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'update.html',d)

def delete(request, pk):
    Tobj = Todo.objects.get(pk=pk)
    Tobj.delete()
    
    return HttpResponseRedirect(reverse('home'))
