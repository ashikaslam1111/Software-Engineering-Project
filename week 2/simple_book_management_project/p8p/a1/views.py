from django.shortcuts import render,redirect
from a1.models import Book_modle
from a1.forms import Book_form
# Create your views here.

def home(request):
    return render(request,'base.html')



def show_data(request):
    data = Book_modle.objects.all()
    return render(request,'show.html',{'data':data})



def store(requset):
    form = Book_form(requset.POST)
    if requset.method=='POST':
         print(2)
         if form.is_valid():
               form.save(commit=True)
               return render(requset,'store.html',{'form':form})
    else :
         print(1)
         form = Book_form()
         return render(requset,'store.html',{'form':form})
     
     
def delete(request,id):
    book = Book_modle.objects.get(pk =  id)
    book.delete()
    return redirect('show')



def edit(request,id):
     book = Book_modle.objects.get(pk =  id)
     form= Book_form(instance=book)
     if request.method == 'POST':
         form= Book_form(request.POST,instance=book)
         if form.is_valid():
             book.save()
             return  redirect('show')
             
     
     return render(request,'store.html',{'form':form})
     
     
     
     
   
     
     
     
    