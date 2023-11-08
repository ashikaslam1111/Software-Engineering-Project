from django import forms
from a1.models import StudentMOdel

class StudentForm(forms.ModelForm):
    class  Meta:
        
        model = StudentMOdel
        fields = '__all__'
        labels={
            'name':'student name',
            
            
        }
        widgets = {
            
            
            
        }
        
        help_text ={
            
            'name':'enter your name'
            
        }
        