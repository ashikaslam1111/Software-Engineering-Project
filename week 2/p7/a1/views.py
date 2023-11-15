from django.shortcuts import render
from a1.forms import StudentForm
from a1.models import Teacher,Students
# Create your views here.


def home(requset):
    
    if requset.method == 'POST':
         std = StudentForm(requset.POST)
         if std.is_valid():
             std.save(commit=True)
             print(std.cleaned_data)
             return render(requset,'index.html',{'from':std})
             
    
        
    else  : std = StudentForm()
    return render(requset,'index.html',{'from':std})





def show(request):
    # stu for every tech
    tech = Teacher.objects.get(name='pritis')
    print(tech)
    stu = tech.stu.all()
    for i in stu:print(i)
    
    
    # teach for every stu
    
    stu = Students.objects.get(name='Ashik')
    tech = stu.teacher_set.all()
    print(tech)
    
    
    
    
    
    return render(request,'show.html')
    
