from django.shortcuts import render,redirect
from. import models
from django.http import HttpResponse
# Create your views here.


def hello(request):
    students = models.Student.objects.all()
    return render(request,'index.html',context={'stu':students})




def delete_stu(request,roll):
    std = models.Student.objects.get(pk = roll).delete()
    print(std)
   
    
    return redirect("homepage")