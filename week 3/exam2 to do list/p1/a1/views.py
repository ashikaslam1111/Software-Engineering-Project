<<<<<<< HEAD
=======

    
>>>>>>> 42c1c1ec1fc17d5941a8e676cd1932d5424b9de0
from django.shortcuts import render,redirect,get_object_or_404
from a1.models import MyTask
from .import forms 
from django.contrib import messages
from  django.views.generic import DetailView
from datetime import datetime





def home(request): # this is for showing my current task
    data = MyTask.objects.filter(status='INCOMPLETED')
    return render(request,'base.html',{'data':data})


def see_done_task(request): # this is for showing my completed task
    data = MyTask.objects.filter(status='COMPLETED')
    return render(request,'completed.html',{'data':data})


def add_task(request):# this is for adding  new task
    if request.method=="POST":
       form = forms.Task_form(request.POST)
       if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    else:form = forms.Task_form() 
    return render(request,'add.html',{'form':form})



def delete_task(request,id):# this is for remove a task  with any status 
    
      current_jop = MyTask.objects.get(pk=id)
      current_jop.delete()
      messages.success(request,'deletion complete!')
      
      return redirect('home')
  
  

class Task_details(DetailView): # this for show details of a task 
    template_name = 'details.html'
    model =  MyTask
    context_object_name = 'i'
    pk_url_kwarg = 'id'
    
    
def edit_task(request, id):
    task = get_object_or_404(MyTask, pk=id)
    form = forms.Task_form(instance=task)

    if request.method == 'POST':
        form = forms.Task_form(request.POST, instance=task)
        if form.is_valid():
            task.edit_count = F('edit_count') + 1
            task.save()
            return redirect('home')

    return render(request, 'add.html', {'form': form})

    
    
   
   
   
def make_completed_a_task(request,id):# make the job complete
   
    task = get_object_or_404(MyTask,pk = id)
    task.status = 'COMPLETED'
    task.finished_date = datetime.now()
    task.save()
    return redirect('home')
     
    
    
    
    
   
   
   
def make_completed_a_task(request,id):# make the job complete
    task = get_object_or_404(MyTask,pk = id)
    task.status = 'COMPLETED'
    task.finished_date = datetime.now()
    task.save()
    return redirect('home')
     
    
    
