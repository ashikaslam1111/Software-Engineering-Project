# my code 



from typing import Any, Dict
from django import forms
from django.core import validators

# class Student(forms.Form):
#     name = forms.CharField()
#     email = forms.CharField()

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Name must be at least 10 characters.")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in  valemail:
    #         raise forms.ValidationError("email must have .com")
    #     return  valemail
    
    # def clean(self):
    #     self.x = super().clean()
    #     valname = self.x['name']
    #     if len(valname) < 10:
    #          raise forms.ValidationError("Name must be at least 10 characters.")
    #     valemail = self.x['email']
    #     if '.com' not in  valemail:
    #          raise forms.ValidationError("email must have .com")

    
def len_cak(value):
    if len(value)>10:
        raise forms.ValidationError("atmost 10 cahr")

    
class Student(forms.Form):
      name = forms.CharField(validators=[validators.MaxLengthValidator(10,message="name cna be at most 10 char")])
      email= forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='enter correct email')])  
      age  = forms.IntegerField(validators=[validators.MinValueValidator(10,message='age should be atleast 10'),validators.MaxValueValidator(35,message='can be at most 35')])
      text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'must be in 10 char'}),validators=[len_cak])
      file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'],message='only pdf or jpg')])
    
    
    

# widgets = field to heml input
class contact_form(forms.Form):
    name = forms.CharField(label="user name",help_text="must be in 70"
      ,required=False,disabled=True  ,widget=forms.Textarea (attrs={'id':'text','placeholder':'enter your name'})          )
    email = forms.EmailField(label="user email")
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    bllence = forms.DecimalField()
    check = forms.BooleanField()
    bithday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    choices = [('s',"small"),('m',"medium"),('l',"large")]
    size = forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    
    meal =  [('s',"sosa"),('m',"moriz"),('l',"lebu")]
    food = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    #file  = forms.FileField()
    
    
    
    
    
    
    
    
class Pass_project(forms.Form):
    name = forms.CharField()
    pas = forms.CharField(widget=forms.PasswordInput)
    re_pas = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
      data =  super().clean()
      valname = data['name']
      valpass = data['pas']
      re_valpass = data['re_pas']
      if len(valname)<5:raise forms.ValidationError("atleast 5 char")
      if valpass != re_valpass: raise forms.ValidationError("pass not same")
      
      
    
    