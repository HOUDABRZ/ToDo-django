from django.shortcuts import render

from django.shortcuts import redirect

# Create your views here.
tasks = []
def index(request):
  return render(request, "list/index.html",{
    "tasks":tasks
  })
  
def addTask(request):
  if request.method=="POST":
    task= request.POST['task']
    tasks.append(task)
    return redirect('index')
    
  else:
        # Handle GET request (display the form)
        return redirect('index')
  
  
def delete(request,id):
  if 0 <= id < len(tasks):
    tasks.pop(id)
  
  return redirect('index')
    
