from django.shortcuts import render
from.form import contact_form
from.form import Student
# Create your views here.

# def student(request):
#     if request.method == 'POST':
#             form  = Student(request.POST)
#             if form.is_valid():
             
#               print(form.cleaned_data)
#               return render(request,'stu.html',{'form':form})
#     form  = Student()
#     return render(request,'stu.html',{'form':form})
    
    
    
from django.shortcuts import render
from .form import Student

def student(request):
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'stu.html', {'form': form})
    else:
        form = Student()
    return render(request, 'stu.html', {'form': form})



def home(request):
    return render(request,'home.html')

def about(request):
    if(request.method == 'POST'):
        print(request.POST)
        print(101)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'about.html',{'name':name,'email':email,'select':select})
    return render(request,'about.html')
       

def form(request):
    
    print(102)  
   ## print(request.POST) 
    return render(request,'form.html')


def django_form(request):
    if request.method == 'POST':
            print(1010)
            form  = contact_form(request.POST,request.FILES)
            if form.is_valid():
              #file = form.cleaned_data['file']
              print(form.cleaned_data)
              #eturn render(request,'dj.html',{'form':form})
    form  = contact_form()
    return render(request,'dj.html',{'form':form})
              