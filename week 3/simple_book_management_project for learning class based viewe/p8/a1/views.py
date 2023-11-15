from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render,redirect
from a1.forms import Book_store_form
from . models import Book_store_model
from  django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
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
    
   
   
   
   
# class based view ------

class MyTemplateView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        contex = super().get_context_data(**kwargs)
        contex ={'name':'aslam','age':19}
        print(kwargs)
        contex.update(kwargs)
        return contex 
    
    
# show 


class Show_book(ListView):
    model = Book_store_model
    template_name = 'show_book.html'
    context_object_name = 'data'
    ordering = ['catagory','id']
    # # def get_queryset(self):
    # #     return Book_store_model.objects.filter(catagory='Thriller')
    # def get_context_data(self, **kwargs):
    #      contex= super().get_context_data( **kwargs)
    #      #contex = {'book':Book_store_model.objects.filter(catagory='Thriller')}
    #      contex = {'book':Book_store_model.objects.all().order_by('author')}
    #      return contex
          
        
       
class Book_detail(DetailView):
    model = Book_store_model
    template_name= 'bookdetails.html'
    context_object_name = 'i'
    pk_url_kwarg = 'id'
    
    
    
    
# class Form_show(FormView):
#     template_name = 'store_book.html'
#     form_class = Book_store_form
#     success_url = reverse_lazy('show')
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('show')

class Form_show(CreateView):
    template_name = 'store_book.html'
    form_class = Book_store_form
    model = Book_store_model
   
    success_url = reverse_lazy('show')
    
    


class update_book(UpdateView):
     form_class = Book_store_form
     template_name = 'store_book.html'
     
     model = Book_store_model
     success_url = reverse_lazy('show')
    
   
        
        
class Delete_book(DeleteView):
     model = Book_store_model
     template_name = 'confirm_delete.html'
     success_url = reverse_lazy('show')
    


