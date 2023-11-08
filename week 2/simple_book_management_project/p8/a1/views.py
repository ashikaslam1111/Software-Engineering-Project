from django.shortcuts import render,redirect
from a1.forms import Book_store_form
from . models import Book_store_model
# Create your views here.

def home(request):
   
    return render(request,'base.html')




def store(request):
    form = Book_store_form(request.POST)
    if request.method == 'POST':
        if form.is_valid(): 
           form.save(commit=True)
           print(form.cleaned_data)
           print(type(form.cleaned_data))
           return render(request,'store_book.html',{'form':form})
       
       
    else :
         
          form = Book_store_form()
          return render(request,'store_book.html',{'form':form})
   
      
      
def show(request):
    data = Book_store_model.objects.all()
    return render(request,'show_book.html',{'data':data})   






def edit(request,id):
    book =  Book_store_model.objects.get(pk = id)
    form = Book_store_form(instance=book)
    if request.method == 'POST':
      book =   Book_store_form(request.POST,instance=book)
      if book.is_valid():
          book.save()
          return  redirect('show')
    
    
    return render(request,'store_book.html',{'form':form})





def delete(request,id):
     book =  Book_store_model.objects.get(pk = id)
     book.delete()
     return redirect('show')
    
    