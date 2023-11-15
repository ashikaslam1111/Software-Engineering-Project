from django import forms
from a1.models import Book_store_model


class Book_store_form(forms.ModelForm):
    
    class Meta:
        model = Book_store_model
       # exclude = ['first_pub','last_pub']
        fields =['id','name','author','catagory']
        
        
        