from django.shortcuts import render
from a1.forms import StudentForm
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