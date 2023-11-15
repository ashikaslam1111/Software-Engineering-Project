from django import forms
from a1.models import MyTask



class Task_form(forms.ModelForm):# this is for taking input from user
    class Meta:
      model =MyTask
      fields =['title', 'description', 'category', ]
     
      
      
      
