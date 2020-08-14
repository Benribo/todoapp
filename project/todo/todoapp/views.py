from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import TodoItem
# Create your views here.
def todoview(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'view.html',{'all_items':all_todo_items})

def addTodo(request):
    new_item=TodoItem(content = request.post["content"])
    new_item.save()
    return HttpResponseRedirect('/todo/')    

def mainpage(request):
  return HttpResponse('hi welcome use /todo near the url to proceed')